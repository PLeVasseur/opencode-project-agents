#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


EXIT_VALIDATION = 2
EXIT_GH = 3
EXIT_MAPPING = 4

NUMBERED_FILE_RE = re.compile(r"^(\d{2})-.+\.md$")
HUNK_HEADER_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,\d+)? @@")


class ReviewToolError(Exception):
    """Base exception for predictable script failures."""


class ValidationError(ReviewToolError):
    """Raised when local inputs are invalid."""


class MappingError(ReviewToolError):
    """Raised when file/line resolution cannot be completed safely."""


class GhError(ReviewToolError):
    """Raised when a gh command fails."""

    def __init__(self, command: list[str], returncode: int, stdout: str, stderr: str):
        self.command = command
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        details = stderr.strip() or stdout.strip() or "(no output)"
        super().__init__(
            f"gh command failed ({returncode}): {' '.join(command)}\n{details}"
        )


@dataclass
class InlineFeedback:
    source_path: Path
    target_file: str
    line_start: int
    line_end: int
    context: str
    body: str
    resolved_path: str | None = None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Create a pending GitHub PR review from split feedback files "
            "(posts inline comments from 01+ files only)."
        )
    )
    parser.add_argument("--pr", type=int, required=True, help="Pull request number")
    parser.add_argument(
        "--feedback-dir",
        required=True,
        help="Directory containing split review files (00-summary.md, 01-*.md, ...)",
    )
    parser.add_argument(
        "--repo",
        help="Optional OWNER/REPO override for gh commands",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be posted (default)",
    )
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Create pending review comments",
    )
    parser.add_argument(
        "--replace-pending",
        dest="replace_pending",
        action="store_true",
        default=True,
        help="Delete your existing pending reviews before creating a new one (default)",
    )
    parser.add_argument(
        "--no-replace-pending",
        dest="replace_pending",
        action="store_false",
        help="Keep existing pending reviews and create an additional pending review",
    )
    args = parser.parse_args()

    if not args.apply:
        args.dry_run = True

    return args


def run_command(
    command: list[str],
    *,
    input_text: str | None = None,
    gh_repo: str | None = None,
) -> str:
    env = None
    if gh_repo:
        env = os.environ.copy()
        env["GH_REPO"] = gh_repo

    proc = subprocess.run(
        command,
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
        env=env,
    )
    if proc.returncode != 0:
        raise GhError(command, proc.returncode, proc.stdout, proc.stderr)
    return proc.stdout


def gh_api_json(
    endpoint: str,
    *,
    repo: str | None,
    method: str = "GET",
    payload: dict[str, Any] | None = None,
    paginate: bool = False,
    slurp: bool = False,
) -> Any:
    command = ["gh", "api", endpoint]
    if method != "GET":
        command.extend(["--method", method])
    if paginate:
        command.append("--paginate")
    if slurp:
        command.append("--slurp")

    input_text = None
    if payload is not None:
        command.extend(["--input", "-"])
        input_text = json.dumps(payload)

    raw = run_command(command, input_text=input_text, gh_repo=repo)
    try:
        return json.loads(raw or "null")
    except json.JSONDecodeError as exc:
        raise ValidationError(
            f"Unable to parse JSON response for endpoint '{endpoint}': {exc}"
        ) from exc


def flatten_slurped_pages(data: Any, *, endpoint: str) -> list[dict[str, Any]]:
    if not isinstance(data, list):
        raise ValidationError(
            f"Expected slurped list from '{endpoint}', got {type(data).__name__}"
        )
    flattened: list[dict[str, Any]] = []
    for page in data:
        if not isinstance(page, list):
            raise ValidationError(
                f"Expected each slurped page from '{endpoint}' to be a list"
            )
        for item in page:
            if not isinstance(item, dict):
                raise ValidationError(
                    f"Expected each item from '{endpoint}' to be an object"
                )
            flattened.append(item)
    return flattened


def parse_positive_int(value: Any, *, field_name: str, source_path: Path) -> int:
    if isinstance(value, bool):
        raise ValidationError(f"{source_path}: '{field_name}' cannot be a boolean")
    try:
        parsed = int(value)
    except (TypeError, ValueError) as exc:
        raise ValidationError(
            f"{source_path}: '{field_name}' must be a positive integer"
        ) from exc
    if parsed <= 0:
        raise ValidationError(
            f"{source_path}: '{field_name}' must be greater than zero"
        )
    return parsed


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValidationError(f"{path}: missing YAML frontmatter opening delimiter")

    end_idx: int | None = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        raise ValidationError(f"{path}: missing YAML frontmatter closing delimiter")

    meta_text = "\n".join(lines[1:end_idx])
    body_text = "\n".join(lines[end_idx + 1 :]).strip()

    try:
        meta = yaml.safe_load(meta_text) if meta_text.strip() else {}
    except yaml.YAMLError as exc:
        raise ValidationError(f"{path}: invalid YAML frontmatter ({exc})") from exc

    if meta is None:
        meta = {}
    if not isinstance(meta, dict):
        raise ValidationError(f"{path}: frontmatter must be a key/value object")

    return meta, body_text


def numbered_markdown_files(feedback_dir: Path) -> list[Path]:
    files = [p for p in feedback_dir.glob("*.md") if p.is_file()]

    def sort_key(path: Path) -> tuple[int, int, str]:
        match = NUMBERED_FILE_RE.match(path.name)
        if not match:
            return (1, 999_999, path.name)
        return (0, int(match.group(1)), path.name)

    return sorted(files, key=sort_key)


def load_inline_feedback(
    feedback_dir: Path,
    *,
    expected_pr: int,
) -> tuple[list[InlineFeedback], list[tuple[str, str]]]:
    if not feedback_dir.exists() or not feedback_dir.is_dir():
        raise ValidationError(f"Feedback directory does not exist: {feedback_dir}")

    inline_feedback: list[InlineFeedback] = []
    skipped: list[tuple[str, str]] = []

    for file_path in numbered_markdown_files(feedback_dir):
        match = NUMBERED_FILE_RE.match(file_path.name)
        if not match:
            skipped.append((file_path.name, "not a numbered issue file"))
            continue

        number_prefix = int(match.group(1))
        if number_prefix == 0 or file_path.name == "00-summary.md":
            skipped.append((file_path.name, "summary file"))
            continue

        meta, body = parse_frontmatter(file_path)

        if "pr" in meta and meta["pr"] is not None:
            pr_value = parse_positive_int(meta["pr"], field_name="pr", source_path=file_path)
            if pr_value != expected_pr:
                raise ValidationError(
                    f"{file_path}: frontmatter pr={pr_value} does not match --pr {expected_pr}"
                )

        comment_type = str(meta.get("comment_type", "")).strip().lower()
        if comment_type == "general":
            skipped.append((file_path.name, "comment_type general"))
            continue
        if comment_type != "inline":
            raise ValidationError(
                f"{file_path}: expected comment_type 'inline' for numbered issue file"
            )

        target_file = meta.get("target_file")
        if not isinstance(target_file, str) or not target_file.strip():
            raise ValidationError(f"{file_path}: missing or invalid 'target_file'")

        context_value = meta.get("context")
        if not isinstance(context_value, str) or not context_value.strip():
            raise ValidationError(f"{file_path}: missing or invalid 'context'")

        line_start = parse_positive_int(
            meta.get("line_start"), field_name="line_start", source_path=file_path
        )
        line_end = parse_positive_int(
            meta.get("line_end"), field_name="line_end", source_path=file_path
        )
        if line_end < line_start:
            raise ValidationError(
                f"{file_path}: line_end ({line_end}) must be >= line_start ({line_start})"
            )

        if not body:
            raise ValidationError(f"{file_path}: comment body cannot be empty")

        inline_feedback.append(
            InlineFeedback(
                source_path=file_path,
                target_file=target_file.strip(),
                line_start=line_start,
                line_end=line_end,
                context=context_value.strip(),
                body=body,
            )
        )

    return inline_feedback, skipped


def resolve_feedback_dir_argument(raw_path: str) -> Path:
    candidate = Path(os.path.expandvars(raw_path)).expanduser()
    if candidate.is_absolute():
        return candidate.resolve()

    cwd_candidate = (Path.cwd() / candidate).resolve()
    if cwd_candidate.exists():
        return cwd_candidate

    config_dir = os.environ.get("OPENCODE_CONFIG_DIR")
    if config_dir:
        config_candidate = (Path(config_dir).expanduser() / candidate).resolve()
        if config_candidate.exists():
            return config_candidate

    return cwd_candidate


def normalize_target_path(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def resolve_target_file(target: str, changed_paths: list[str]) -> str:
    normalized_target = normalize_target_path(target)

    exact_matches = [path for path in changed_paths if path == normalized_target]
    if len(exact_matches) == 1:
        return exact_matches[0]

    suffix_matches = [path for path in changed_paths if path.endswith(f"/{normalized_target}")]
    if len(suffix_matches) == 1:
        return suffix_matches[0]
    if len(suffix_matches) > 1:
        joined = ", ".join(sorted(suffix_matches))
        raise MappingError(
            f"Ambiguous target_file '{target}'. Matches multiple changed files: {joined}"
        )

    raise MappingError(
        f"target_file '{target}' did not match any changed file in the PR"
    )


def parse_right_side_lines_from_patch(patch: str) -> set[int]:
    right_lines: set[int] = set()
    current_right_line: int | None = None

    for line in patch.splitlines():
        if line.startswith("@@"):
            match = HUNK_HEADER_RE.match(line)
            if not match:
                current_right_line = None
                continue
            current_right_line = int(match.group(1))
            continue

        if current_right_line is None:
            continue

        if line.startswith("+") and not line.startswith("+++"):
            right_lines.add(current_right_line)
            current_right_line += 1
            continue

        if line.startswith(" "):
            right_lines.add(current_right_line)
            current_right_line += 1
            continue

        if line.startswith("-"):
            continue

        if line.startswith("\\"):
            continue

    return right_lines


def build_patch_line_map(pr_files: list[dict[str, Any]]) -> dict[str, set[int] | None]:
    line_map: dict[str, set[int] | None] = {}
    for pr_file in pr_files:
        filename = pr_file.get("filename")
        patch = pr_file.get("patch")
        if not isinstance(filename, str):
            continue
        if isinstance(patch, str):
            line_map[filename] = parse_right_side_lines_from_patch(patch)
        else:
            line_map[filename] = None
    return line_map


def validate_comment_anchors(
    comments: list[InlineFeedback],
    *,
    patch_line_map: dict[str, set[int] | None],
) -> None:
    for comment in comments:
        if comment.resolved_path is None:
            raise MappingError(
                f"{comment.source_path.name}: internal error, unresolved file mapping"
            )
        lines = patch_line_map.get(comment.resolved_path)
        if lines is None:
            raise MappingError(
                f"{comment.source_path.name}: no textual patch available for "
                f"{comment.resolved_path}; cannot validate line anchors"
            )
        if comment.line_start not in lines:
            raise MappingError(
                f"{comment.source_path.name}: line_start {comment.line_start} is not "
                f"commentable on RIGHT side for {comment.resolved_path}"
            )
        if comment.line_end not in lines:
            raise MappingError(
                f"{comment.source_path.name}: line_end {comment.line_end} is not "
                f"commentable on RIGHT side for {comment.resolved_path}"
            )


def build_review_payload(commit_sha: str, comments: list[InlineFeedback]) -> dict[str, Any]:
    payload_comments = []
    for comment in comments:
        if comment.resolved_path is None:
            raise MappingError(
                f"{comment.source_path.name}: internal error, unresolved file mapping"
            )
        payload_comments.append(
            {
                "path": comment.resolved_path,
                "line": comment.line_start,
                "side": "RIGHT",
                "body": comment.body,
            }
        )
    return {
        "commit_id": commit_sha,
        "comments": payload_comments,
    }


def first_line_snippet(text: str, *, width: int = 110) -> str:
    first_line = text.splitlines()[0].strip() if text.splitlines() else ""
    if len(first_line) <= width:
        return first_line
    return first_line[: width - 3] + "..."


def render_comment_table(comments: list[InlineFeedback]) -> str:
    rows = []
    for index, comment in enumerate(comments, start=1):
        rows.append(
            (
                f"{index:02d}",
                comment.source_path.name,
                f"{comment.resolved_path}:{comment.line_start}",
                first_line_snippet(comment.body),
            )
        )
    if not rows:
        return "(none)"

    col1 = max(len(row[0]) for row in rows)
    col2 = max(len(row[1]) for row in rows)
    col3 = max(len(row[2]) for row in rows)

    lines = []
    for row in rows:
        lines.append(
            f"{row[0].ljust(col1)}  {row[1].ljust(col2)}  {row[2].ljust(col3)}  {row[3]}"
        )
    return "\n".join(lines)


def load_pr_state(
    pr_number: int,
    *,
    repo: str | None,
) -> tuple[str, str, list[dict[str, Any]]]:
    pr_endpoint = f"repos/{{owner}}/{{repo}}/pulls/{pr_number}"
    pr_data = gh_api_json(pr_endpoint, repo=repo)
    if not isinstance(pr_data, dict):
        raise ValidationError(f"Unexpected PR payload type: {type(pr_data).__name__}")

    commit_sha = (
        pr_data.get("head", {}).get("sha") if isinstance(pr_data.get("head"), dict) else None
    )
    pr_url = pr_data.get("html_url")
    if not isinstance(commit_sha, str) or not commit_sha:
        raise ValidationError("Unable to read PR head commit SHA")
    if not isinstance(pr_url, str) or not pr_url:
        raise ValidationError("Unable to read PR URL")

    files_endpoint = f"repos/{{owner}}/{{repo}}/pulls/{pr_number}/files?per_page=100"
    files_slurped = gh_api_json(
        files_endpoint,
        repo=repo,
        paginate=True,
        slurp=True,
    )
    pr_files = flatten_slurped_pages(files_slurped, endpoint=files_endpoint)

    return commit_sha, pr_url, pr_files


def current_login() -> str:
    user_data = gh_api_json("user", repo=None)
    if not isinstance(user_data, dict) or not isinstance(user_data.get("login"), str):
        raise ValidationError("Unable to determine current GitHub login")
    return user_data["login"]


def delete_pending_reviews(
    *,
    pr_number: int,
    repo: str | None,
    login: str,
) -> list[int]:
    endpoint = f"repos/{{owner}}/{{repo}}/pulls/{pr_number}/reviews?per_page=100"
    reviews = gh_api_json(endpoint, repo=repo)
    if not isinstance(reviews, list):
        raise ValidationError("Unexpected reviews payload while deleting pending reviews")

    deleted_ids: list[int] = []
    for review in reviews:
        if not isinstance(review, dict):
            continue
        state = review.get("state")
        review_id = review.get("id")
        user = review.get("user")
        review_login = user.get("login") if isinstance(user, dict) else None

        if state != "PENDING" or review_login != login:
            continue
        if not isinstance(review_id, int):
            continue

        delete_endpoint = f"repos/{{owner}}/{{repo}}/pulls/{pr_number}/reviews/{review_id}"
        gh_api_json(delete_endpoint, repo=repo, method="DELETE")
        deleted_ids.append(review_id)

    return deleted_ids


def create_pending_review(
    *,
    pr_number: int,
    repo: str | None,
    payload: dict[str, Any],
) -> dict[str, Any]:
    endpoint = f"repos/{{owner}}/{{repo}}/pulls/{pr_number}/reviews"
    response = gh_api_json(endpoint, repo=repo, method="POST", payload=payload)
    if not isinstance(response, dict):
        raise ValidationError("Unexpected create-review response payload")
    return response


def main() -> int:
    args = parse_args()

    feedback_dir = resolve_feedback_dir_argument(args.feedback_dir)

    try:
        comments, skipped = load_inline_feedback(feedback_dir, expected_pr=args.pr)
        if not comments:
            output_lines = [
                f"Mode: {'apply' if args.apply else 'dry-run'}",
                f"PR: #{args.pr}",
                f"Feedback directory: {feedback_dir}",
                "Inline comments ready: 0",
                "No inline issue files were found to post.",
            ]
            if skipped:
                output_lines.append("Skipped files:")
                for name, reason in skipped:
                    output_lines.append(f"- {name}: {reason}")
            print("\n".join(output_lines))
            return 0

        commit_sha, pr_url, pr_files = load_pr_state(args.pr, repo=args.repo)
        changed_paths: list[str] = []
        for pr_file in pr_files:
            filename = pr_file.get("filename")
            if isinstance(filename, str):
                changed_paths.append(filename)

        for comment in comments:
            comment.resolved_path = resolve_target_file(comment.target_file, changed_paths)

        patch_line_map = build_patch_line_map(pr_files)
        validate_comment_anchors(comments, patch_line_map=patch_line_map)

        payload = build_review_payload(commit_sha, comments)

        output_lines = [
            f"Mode: {'apply' if args.apply else 'dry-run'}",
            f"PR: #{args.pr}",
            f"PR URL: {pr_url}",
            f"Feedback directory: {feedback_dir}",
            f"Inline comments ready: {len(comments)}",
        ]

        if skipped:
            output_lines.append("Skipped files:")
            for name, reason in skipped:
                output_lines.append(f"- {name}: {reason}")

        output_lines.append("Resolved inline comments:")
        output_lines.append(render_comment_table(comments))

        if args.dry_run:
            output_lines.append("Review payload preview:")
            output_lines.append(json.dumps(payload, indent=2))
            print("\n".join(output_lines))
            return 0

        deleted_ids: list[int] = []
        if args.replace_pending:
            login = current_login()
            deleted_ids = delete_pending_reviews(pr_number=args.pr, repo=args.repo, login=login)

        review = create_pending_review(pr_number=args.pr, repo=args.repo, payload=payload)

        review_id = review.get("id")
        review_state = review.get("state")

        if deleted_ids:
            output_lines.append(
                "Deleted existing pending review IDs: "
                + ", ".join(str(review_id) for review_id in deleted_ids)
            )
        else:
            output_lines.append("Deleted existing pending review IDs: none")

        output_lines.append(f"Created pending review ID: {review_id}")
        output_lines.append(f"Created review state: {review_state}")
        output_lines.append(f"Posted inline comments: {len(comments)}")
        output_lines.append(f"Next step: gh pr view {args.pr} --web")

        print("\n".join(output_lines))
        return 0

    except ValidationError as exc:
        print(f"Validation error: {exc}", file=sys.stderr)
        return EXIT_VALIDATION
    except MappingError as exc:
        print(f"Mapping error: {exc}", file=sys.stderr)
        return EXIT_MAPPING
    except GhError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_GH


if __name__ == "__main__":
    sys.exit(main())

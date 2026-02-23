import { tool } from "@opencode-ai/plugin"
import { spawnSync } from "node:child_process"
import path from "node:path"
import { fileURLToPath } from "node:url"

const TOOL_DIR = path.dirname(fileURLToPath(import.meta.url))
const SCRIPT_PATH = path.join(TOOL_DIR, "pr_review_draft.py")

export default tool({
  description:
    "Create or preview pending inline PR review comments from split feedback files",
  args: {
    pr: tool.schema
      .number()
      .int()
      .positive()
      .describe("Pull request number"),
    feedback_dir: tool.schema
      .string()
      .min(1)
      .describe("Path to split feedback directory"),
    apply: tool.schema
      .boolean()
      .optional()
      .default(false)
      .describe("When true, post pending review comments; otherwise run dry-run"),
    replace_pending: tool.schema
      .boolean()
      .optional()
      .default(true)
      .describe("Delete your existing pending reviews before creating a new one"),
    repo: tool.schema
      .string()
      .optional()
      .describe("Optional OWNER/REPO override"),
  },
  async execute(args, context) {
    const command = [
      SCRIPT_PATH,
      "--pr",
      String(args.pr),
      "--feedback-dir",
      args.feedback_dir,
      args.apply ? "--apply" : "--dry-run",
      args.replace_pending ? "--replace-pending" : "--no-replace-pending",
    ]

    if (args.repo) {
      command.push("--repo", args.repo)
    }

    const result = spawnSync("python3", command, {
      cwd: context.directory,
      encoding: "utf8",
      env: process.env,
    })

    if (result.error) {
      throw new Error(`Failed to launch pr_review_draft.py: ${result.error.message}`)
    }

    const stdout = (result.stdout || "").trim()
    const stderr = (result.stderr || "").trim()

    if (result.status !== 0) {
      const details = stderr || stdout || "No output returned"
      throw new Error(
        `pr-review-draft failed with exit code ${result.status}\n${details}`,
      )
    }

    return stdout || "pr-review-draft completed with no output"
  },
})

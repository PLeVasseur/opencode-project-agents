# Glossary parallel wrapper plan

Goal: add a heartbeat/status display to the wrapper that tracks per-letter runs, finalize status, and reminds how to view status in a browser.

## Scope
- Wrapper script lives at `$OPENCODE_CONFIG_DIR/glossary-parallel.sh`.
- Heartbeat runs while any per-letter job is active or finalize is pending/running.
- Status uses per-letter session IDs `glossary-<LETTER>`.

## Plan
- [x] Define heartbeat output format.
  - Include per-letter status: `running`, `success`, `failed`, `unknown`.
  - Include finalize status: `pending`, `running`, `done`, `skipped`.
  - Include a “next check in N seconds” line.
  - Include a reminder for browser monitoring (see below).
- [x] Decide data source for status.
  - If `--attach <url>` is used: query `GET <url>/session/status` and map session IDs to letters.
  - If no attach URL: fall back to tracked PIDs/exit codes for each letter.
  - Keep a simple in-script status table for letters (PID, start time, exit code).
- [x] Implement heartbeat loop.
  - Default interval: 30s (configurable via `--heartbeat <seconds>`).
  - Print status to stdout and append to a log file in the shared config dir.
  - End the heartbeat once all letter runs and optional finalize are complete.
- [x] Add a browser status reminder in each heartbeat.
  - If `--attach` URL provided: print `Open Web UI: opencode web --port <port> && open http://<host>:<port>` or the current server URL if using `opencode web`.
  - Otherwise: print `Start Web UI with: opencode web` and note that sessions are visible on the homepage.
- [x] Track finalize progress.
  - Record finalize PID and exit code when `--finalize` is requested.
  - Show finalize status in the heartbeat and final summary.
- [x] Update wrapper help/usage.
  - Added `--discover` to probe `/global/health` and match `/project/current`.

## Debug run
- [x] Run the wrapper with `--next Q R S T --discover --finalize --heartbeat 10`.
- [x] Watch `parallel-heartbeat-<RUN_ID>.log` and per-letter logs for errors.
- [x] Fix any script errors and re-run until launches succeed.
  - Document `--heartbeat` and the monitoring reminders.
  - Document that shared backend uses distinct `--session` IDs per letter.

## Notes
- The server API is documented at `https://opencode.ai/docs/server` (`/session/status` and `/event` endpoints).
- Web UI session view is documented at `https://opencode.ai/docs/web`.

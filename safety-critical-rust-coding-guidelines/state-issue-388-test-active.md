## Reviewer Bot State (test)

> WARNING: DO NOT EDIT MANUALLY - This issue is automatically maintained by the reviewer bot.
> Use bot commands instead (see CONTRIBUTING.md for details).

This issue tracks the round-robin assignment of reviewers for coding guidelines.

### Current State

```yaml
last_updated: null
current_index: 0
queue: []
pass_until: []
recent_assignments: []
active_reviews:
  "7":
    skipped: []
    current_reviewer: PLeVasseur
    assigned_at: 2026-02-04T19:12:16+00:00
    last_reviewer_activity: 2026-02-04T19:12:16+00:00
    transition_warning_sent: null
    assignment_method: manual
    review_completed_at: null
    review_completed_by: null
    review_completion_source: null
```

### What This Tracks

- queue: Active reviewers in rotation order
- current_index: Position in queue (who's next)
- pass_until: Reviewers temporarily away with return dates
- recent_assignments: Last 20 assignments for visibility
- active_reviews: Per-issue/PR tracking of who passed and the current designated reviewer

# Git Workflow

## Role Of Git

Git is the primary mechanism for versioning, review, and rollback in this vault.

- Use it to make changes inspectable.
- Use it to isolate experiments or reorganizations.
- Use it to recover from mistakes without relying on memory.

## Commit Style

Prefer small, coherent commits.

- group changes by operation or intent
- avoid bundling unrelated note edits, renames, and structural changes together
- keep commit scopes narrow enough that another person can understand them from the diff

## Grouping By Operation

When possible, separate different kinds of work.

- intake processing can be grouped separately from semantic note creation
- paper library cleanup can be grouped separately from note linking
- structural reorganization can be grouped separately from content refinement

This makes review and rollback easier.

## Larger Reorganizations

If broader reorganization is needed:

- prefer an isolated branch or worktree
- keep the scope explicit
- avoid mixing large moves with unrelated content edits

Large path changes should be prepared carefully because they carry link and review risk.

## Diff Clarity

Changes should remain understandable in diffs.

- prefer readable filenames and file-local edits
- keep rename and move operations deliberate
- avoid churn that obscures the substantive change

If a proposed change would be hard to review, reduce the scope or split it into smaller steps.

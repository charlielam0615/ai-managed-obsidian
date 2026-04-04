# Safe Change Policy

## Default Change Posture

Agents should prefer conservative, bounded edits.

- Make the smallest change that meaningfully improves the vault.
- Preserve existing information whenever possible.
- Avoid broad restructuring unless the benefit is clear and the scope is controlled.

## Bounded Edits

Changes should stay local and understandable.

- prefer small batches of related edits
- avoid mixing unrelated cleanup and content changes
- keep moves, renames, and semantic edits scoped so they can be reviewed and reversed

## Avoid Forced Classification

Do not force material into a taxonomy just to make it look organized.

- If the right placement is unclear, defer.
- If a note spans multiple themes, prefer links and local metadata over inventing new folders.
- If a paper is not fully understood yet, preserve it without overclassifying it.

## When To Defer

Defer action instead of guessing when:

- the intended destination is genuinely unclear
- a rename would likely break expectations or links
- reorganization would introduce more churn than value
- the change cannot be made confidently in a reviewable way

## Non-Destructive Reorganization

Reorganization must be incremental and reversible.

- Prefer gradual cleanup over vault-wide reshuffles.
- Do not delete or overwrite meaningful content simply because it is messy.
- Keep historical continuity where practical through stable names, clear moves, and Git history.

## Reviewability

All changes should remain understandable in a diff.

- group related edits together
- make rationale legible from the files themselves
- favor operations that can be audited and rolled back cleanly

## General Agent Constraints

Agents operating in this vault should:

- respect the single human intake point in `Inbox/`
- place agent-created content directly in destination folders
- protect link integrity when renaming or moving files
- prefer note and link structure over deep folder expansion

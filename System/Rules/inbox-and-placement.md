# Inbox And Placement

## Inbox Policy

`Inbox/` is the single intake location for new human-created material.

Allowed examples:

- new Markdown notes captured by a human
- rough drafts
- clipped text
- human-added PDFs awaiting processing

`Inbox/` is the unprocessed intake area. It is not yet the integrated knowledge layer.

## One Intake Point

All human-created new material enters through `Inbox/`.

- Do not create additional intake folders.
- Do not split intake by topic, source, or media type.

## Agent Placement Policy

Agents should create new content directly in its destination folder unless explicitly simulating human capture.

- processed notes that are ready for integration belong in `Notes/`
- canonical paper PDFs belong in `Library/Papers/`
- system guidance belongs in `System/`

Agents should not use `Inbox/` as a generic staging area for their own work.

## Relocating Notes And Papers

When processing `Inbox/`, agents should move items only when the destination is reasonably clear.

- move notes into `Notes/` only after they are processed enough to function in the knowledge layer
- move PDF papers into `Library/Papers/` when they are identified as part of the paper corpus
- create or update corresponding paper notes in `Notes/` as the semantic interface to papers

Processing enough means:

- the correct location is chosen
- the required metadata is present
- the note has been incorporated into the relevant index, hub, or navigation surface

Required metadata should follow `System/Rules/processed-note-metadata.md`.

## Handling Uncertainty

Uncertainty should not force premature relocation.

- If a note is still incomplete or ambiguous, it may remain in `Inbox/` until a reasonable placement decision can be made.
- If a paper's metadata is unclear, prefer minimal cleanup and deferred placement decisions over inventing false precision.
- When unsure, preserve the item and add only the minimum structure needed to support later review.

Notes in `Notes/` are still open to future edits, links, metadata changes, and restructuring. Moving a note out of `Inbox/` means it is processed enough for integration, not that it is final.

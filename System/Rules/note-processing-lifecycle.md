# Note Processing Lifecycle

## Purpose

This rule defines the lifecycle distinction between notes in `Inbox/` and notes in `Notes/`.

The distinction is not permanence.

Notes in `Notes/` remain open to future edits, linking, relocation, metadata improvement, and synthesis.

## Core Model

- `Inbox/` holds notes and captures that are not yet fully processed.
- `Notes/` holds notes that are processed enough to participate in the knowledge layer.

Processed enough means:

- the note is in the correct location
- required metadata is present
- the note has been incorporated into the relevant index, hub, or navigation surface

See `System/Rules/processed-note-metadata.md` for the minimum metadata contract.

Fallback order for navigation integration:

1. existing topic hub or overview note
2. existing relevant curated index section
3. bootstrap section in `Notes/Index.md`

## Inbox

`Inbox/` is the intake and pre-integration area.

Items in `Inbox/` may still need:

- better placement
- metadata
- source clarification
- conversion into note-ready form
- incorporation into the note graph

Leaving something in `Inbox/` does not mean it is low value. It means processing is not complete enough yet.

## Notes

`Notes/` is the processed knowledge layer.

Notes in `Notes/` should be:

- ready to participate in retrieval
- ready to receive links and metadata improvements
- ready to be integrated into overviews, hubs, and synthesis notes

They are not final artifacts.

## Continuous Integration

A note does not stop evolving after it enters `Notes/`.

Sleep and other maintenance workflows may continue to:

- add or improve links
- improve metadata
- update navigation surfaces
- strengthen local or cluster-level synthesis
- relocate notes when there is a clear structural benefit

## Processing Bar For Leaving Inbox

A note should leave `Inbox/` only after:

1. the correct destination is chosen
2. the required metadata is present
3. the note is incorporated into the relevant navigation surface

Do not require complete synthesis before moving a note into `Notes/`.

Do require enough processing that the note can be found, understood, and integrated later without returning it to intake status.

If no topic hub or other better navigation surface exists yet, the bootstrap section in `Notes/Index.md` is the default fallback.

## State Relationship

Operational state may record what should be revisited later.

State should help the system remember future integration work, but the actual knowledge must remain in notes, links, metadata, indexes, and other note-layer artifacts.

## Verification

Before treating a note as part of `Notes/`, confirm:

- its placement is justified
- its metadata is sufficient
- its retrieval path exists through the relevant index, hub, or navigation surface
- future edits are still possible without treating the note as fixed

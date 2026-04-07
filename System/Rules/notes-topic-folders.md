# Notes Topic Folders

## Purpose

This rule defines when a topic-specific folder under `Notes/` is justified.

The default posture is to keep `Notes/` relatively flat and improve navigation through links, local metadata, hub notes, overview notes, and the content index before expanding folder hierarchy.

## Default

Do not create a topic folder under `Notes/` merely because a topic has many notes.

Count alone is not sufficient.

Prefer these first:

- improve `Notes/Index.md`
- create or strengthen a topic hub note
- create synthesis or overview notes
- improve aliases and search terms
- improve links between related notes

## When A Topic Folder Is Justified

A topic folder may be justified only when it materially improves retrieval, scanability, maintenance, or reviewability beyond what index and hub-based navigation can provide.

Strong signals include:

- note names in the topic are becoming noisy or collision-prone
- it is becoming materially harder to scan related notes in a flat layout
- review diffs and placement decisions are getting harder because too many adjacent notes are effectively part of one bounded topic region
- the topic has a stable enough boundary that the folder is likely to remain useful
- the folder improves actual workflows more than a stronger hub note or index update would

## When Not To Create One

Do not create a topic folder when:

- the main reason is just note count
- the topic boundary is still fuzzy
- the notes span multiple themes and links would model that better
- a hub note or overview note would solve the problem with less churn
- the change would create broad path churn with weak payoff

If the right answer is still unclear, defer.

## Decision Test

Before creating a topic folder under `Notes/`, confirm all of the following:

1. A flat layout plus better navigation was considered first.
2. The topic has a stable and human-legible boundary.
3. The change will make real retrieval or maintenance tasks easier.
4. The expected benefit is larger than the cost of moves, path churn, and link verification.
5. The reorganization can be performed in a small, reviewable batch.

If any of these are not true, do not create the folder yet.

## Preferred Reorganization Sequence

When topic pressure is rising, prefer this sequence:

1. strengthen the index
2. create or improve a topic hub note
3. create local synthesis or overview notes
4. improve aliases, search terms, and links
5. only then consider a topic folder if the problem remains

This keeps the first response semantic rather than structural.

## Execution Rules

If a topic folder is justified:

- keep the move bounded
- move only the notes that clearly belong
- use Obsidian-aware operations when path semantics matter
- avoid mixing the folder move with unrelated note cleanup
- update the index or hub notes if navigation changes materially

Do not use a folder move as cover for broad renaming or taxonomy cleanup.

## Verification

After creating a topic folder:

- confirm the moved notes now live in the intended destination
- confirm the folder boundary still reads as coherent
- confirm navigation is actually clearer than before
- confirm links and references still behave as expected
- confirm the diff remains reviewable

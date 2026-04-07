---
name: inbox-triage
description: Use this skill when processing material in Inbox/, deciding whether an item is ready for the knowledge layer, a paper candidate, or still unresolved, and relocating it conservatively without forcing classification.
---

# Inbox Triage

## When To Use

Use this skill when new human-created material has landed in `Inbox/` and needs inspection, minimal enrichment, and possible relocation.

## Inputs

- one or more items in `Inbox/`
- any obvious local context about the item's source or intended use
- access to vault search and file inspection, preferably through Obsidian-aware retrieval when practical

## Output

One of:

- a processed note moved into `Notes/`
- a paper candidate handed off to the `paper-ingestion` skill
- an item intentionally left in `Inbox/` with only minimal clarification

## Procedure

1. Inspect the item and identify its basic type.
2. Decide whether it is primarily:
   - a knowledge-layer note candidate
   - a paper or paper candidate
   - an unsupported or unresolved item
3. Add only the minimum enrichment needed to support later placement.
4. Move the item only if the destination is reasonably clear.
5. Leave uncertain items in `Inbox/` instead of forcing classification.

## Minimal Enrichment

Allowed examples:

- clean an obviously noisy title
- add a short note header if a human draft lacks context
- record a likely title, source hint, or status note
- identify whether a PDF appears to be a paper

Do not turn triage into full synthesis, taxonomy building, or broad cleanup.

## Placement Rules

- Move note material to `Notes/` only when it is processed enough to function in the knowledge layer.
- Route paper PDFs through the `paper-ingestion` skill before treating them as canonical library items.
- Do not create new agent work product in `Inbox/` unless explicitly simulating human capture.
- Add the minimum metadata required by `System/Rules/processed-note-metadata.md` before promoting a note into `Notes/`.
- When promoting a non-English processed note into `Notes/`, also add the extra English retrieval bridge required by the language rule.
- Confirm the note is incorporated into the relevant navigation surface before leaving `Inbox/`, using this fallback order:
  - existing topic hub or overview note
  - existing relevant curated index section
  - bootstrap section in `Notes/Index.md`
- Do not invent a new topic hub prematurely just to satisfy the placement rule.
- If follow-up integration work remains after promotion, record one or more queue signals using `System/Skills/sleep/references/signal-writing.md`.

## When Not To Act

Do not relocate an item when:

- the type is still unclear
- the processed destination is uncertain
- the move would imply a classification that is not yet justified
- renaming or moving would create unnecessary churn

In these cases, preserve the item and make only the minimum change needed to support later review.

## Verification

After any relocation:

- confirm the item exists in the destination
- confirm the source copy was not left behind unintentionally
- confirm any note-aware rename or move behaved as expected

If verification is weak, stop before doing more cleanup.

## Related Skills

- `paper-ingestion`
- `obsidian-cli`
- `path-change-policy`

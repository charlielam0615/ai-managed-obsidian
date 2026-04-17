---
name: inbox-triage
description: Use this skill when processing material in Inbox/, digesting note-like items into the knowledge layer, routing source documents appropriately, and leaving only genuinely unsupported or non-note items unresolved.
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
- a document candidate handed off to the `document-ingestion` skill
- an unsupported or non-note item intentionally left in `Inbox/` with only minimal clarification

## Procedure

1. Inspect the item and identify its basic type.
2. Decide whether it is primarily:
   - a knowledge-layer note candidate
   - a source document or document candidate
   - an unsupported or unresolved item
3. Add only the minimum enrichment needed to support later placement.
4. Digest note-like material enough that it can leave `Inbox/` and join the knowledge layer.
5. Move the resulting note into `Notes/`, or route source documents through `document-ingestion`.
6. Leave only genuinely unsupported or non-note items in `Inbox/`.

## Minimal Enrichment

Allowed examples:

- clean an obviously noisy title
- add a short note header if a human draft lacks context
- record a likely title, source hint, or status note
- identify what kind of source document a file appears to be

Do not turn triage into full synthesis, taxonomy building, or broad cleanup.

## Placement Rules

- Move note material to `Notes/` only when it is processed enough to function in the knowledge layer.
- Route PDFs and other source documents through the `document-ingestion` skill before treating them as canonical library items.
- Do not create new agent work product in `Inbox/` unless explicitly simulating human capture.
- Add the minimum metadata required by `System/Rules/processed-note-metadata.md` before promoting a note into `Notes/`.
- When promoting a non-English processed note into `Notes/`, also add the extra English retrieval bridge required by the language rule.
- Confirm the note is incorporated into the relevant navigation surface before leaving `Inbox/`, using this fallback order:
  - existing topic hub or overview note
  - existing relevant curated index section
  - bootstrap section in `Notes/Index.md`
- Treat navigation integration as complete only when a concrete written link exists in that surface.
- If relying on an existing topic hub, overview note, or curated index section, that surface must already link to the promoted note or be updated in the same run.
- If no better navigation surface exists yet, update the bootstrap section in `Notes/Index.md` during the same run rather than treating navigation as implicitly complete.
- Do not invent a new topic hub prematurely just to satisfy the placement rule.
- If the bootstrap section is already at its cap, remove the oldest bootstrap entry that still lacks a better navigation surface rather than blocking promotion.
- If neither a safe existing-surface update nor a safe bootstrap update can be completed in the same run, do not silently treat promotion as complete. Write a sleep signal and report the explicit `Index decision` for the run.
- If follow-up integration work remains after promotion, record one or more queue signals using `System/Skills/sleep/references/signal-writing.md`.

For note-like items, uncertainty is not a reason to leave them in `Inbox/`.

Triage should digest them enough to move them onward.

## When Not To Act

Do not relocate an item when:

- the item is genuinely not note-like
- the item is unsupported in the current system
- the move would imply a classification that is not yet justified
- renaming or moving would create unnecessary churn

In these cases, preserve the item in `Inbox/` and make only the minimum change needed to support later review.

## Verification

After any relocation:

- confirm the item exists in the destination
- confirm the source copy was not left behind unintentionally
- confirm any note-aware rename or move behaved as expected
- confirm the run ended with an explicit `Index decision`: `updated Notes/Index.md`, `used existing navigation surface: <path>`, or `deferred with sleep signal: <signal_id>`
- confirm any unfinished integration work was either completed immediately or captured as one or more sleep queue signals

If verification is weak, stop before doing more cleanup.

## Related Skills

- `document-ingestion`
- `obsidian-cli`
- `path-change-policy`

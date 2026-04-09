---
name: document-ingestion
description: Use this skill when a source document in Inbox/ should be inspected, classified as a document subtype, renamed conservatively, moved into Library/Documents/, and linked to a corresponding note in Notes/.
---

# Document Ingestion

## When To Use

Use this skill when a file in `Inbox/` appears to be a source document that should join the canonical document corpus.

This includes:

- scholarly papers
- reports
- manuals
- whitepapers
- slide decks
- ebooks
- scanned documents
- other reference PDFs or document-like source files

## Inputs

- a source document, usually from `Inbox/`
- whatever metadata or source evidence is available from the file itself
- access to vault search, note inspection, and path changes

## Output

One of:

- a canonical source document in `Library/Documents/` plus a corresponding source note in `Notes/`
- an update to an existing source note or duplicate record
- a deferred decision that leaves the file in `Inbox/` because the evidence is still too weak

## Procedure

1. Confirm the file is a source document appropriate for the canonical document corpus.
2. Identify the likely document subtype when useful, such as:
   - paper
   - report
   - manual
   - slide deck
   - ebook
   - other reference document
3. Extract the minimum useful metadata that can be established with reasonable confidence.
4. Check for likely duplicates in both `Library/Documents/` and `Notes/`.
5. Normalize the filename into a stable, readable canonical form if confidence is sufficient.
6. Move the source document into `Library/Documents/`.
7. Create or update the corresponding source note in `Notes/`.
8. Verify that the note and source document clearly point to the same object.

## Minimum Metadata

Capture what can be established with reasonable confidence:

- title
- creator or author when available
- year or date when clear
- source type or subtype when useful
- stable URL, DOI, or source reference when available

Do not fabricate precise metadata.

## Duplicate Check

Compare using practical signals such as:

- exact or near-exact title
- DOI or stable source URL
- author or creator plus year
- obviously similar normalized filenames

If a likely duplicate exists, prefer updating the existing note or resolving the conflict instead of creating parallel copies.

Use the `obsidian-cli` skill for vault-aware duplicate search and note retrieval when practical.

## Naming And Placement

- Prefer stable, human-readable filenames over importer noise.
- Keep `Library/Documents/` flat by default.
- Do not create subtype or topic folders unless the system changes deliberately later.

If metadata is incomplete, choose the least misleading readable name rather than inventing a rigid naming scheme.

## Source Note

Create or update a corresponding note in `Notes/` that serves as the semantic interface to the source document.

Useful contents include:

- canonical title
- link or reference to the source document
- minimal metadata
- document subtype when useful
- short summary or status when available
- links to related notes if they already exist

Do not require a heavy schema.

The resulting source note should still satisfy the minimum processed-note metadata contract in `System/Rules/processed-note-metadata.md`.

If the resulting source note is primarily non-English, include the minimum English retrieval bridge:

- `lang`
- English `aliases`
- English `search_terms`
- a short English `summary`

If the document appears to be a paper subtype, richer bibliographic metadata is encouraged when available, but it is still handled inside this document workflow.

When integrating the source note into navigation, use this fallback order:

1. existing topic hub or overview note
2. existing curated index section if the source note is genuinely an entry point
3. bootstrap section in `Notes/Index.md` when no better navigation surface exists yet

Update `Notes/Index.md` only when the source note clearly becomes a processed entry point, such as a key source note or a topic anchor. Do not add every ingested document to the index.

Bootstrap fallback is acceptable for ordinary document notes during cold start or hub absence.

If the new or updated source note likely needs later linking, overview integration, or broader sleep digestion, record one or more queue signals using `System/Skills/sleep/references/signal-writing.md`.

## When Not To Act

Defer or narrow the operation when:

- the file is not clearly a source document
- duplicate status is unresolved
- metadata is too uncertain to support a stable rename
- the move would create more churn than value

## Verification

After ingestion:

- confirm the source document exists in `Library/Documents/`
- confirm the source note exists or was updated in `Notes/`
- confirm the note and document still correspond after any rename
- confirm duplicate handling did not create a confusing parallel copy

## Related Skills

- `inbox-triage`
- `obsidian-cli`
- `path-change-policy`

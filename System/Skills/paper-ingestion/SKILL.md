---
name: paper-ingestion
description: Use this skill when a PDF in Inbox/ appears to be a paper and should be checked for duplicates, renamed conservatively, moved into Library/Papers/, and linked to a corresponding note in Notes/.
---

# Paper Ingestion

## When To Use

Use this skill when a PDF appears to be a scholarly or formal source document that may belong in the canonical paper corpus.

## Inputs

- a PDF, usually from `Inbox/`
- whatever bibliographic evidence is available from the file itself
- access to vault search, note inspection, and path changes

## Output

One of:

- a canonical PDF in `Library/Papers/` plus a corresponding paper note in `Notes/`
- an update to an existing paper note or duplicate record
- a deferred decision that leaves the file in `Inbox/` because the evidence is still too weak

## Procedure

1. Confirm the PDF is likely a paper.
2. Extract the minimum useful bibliographic metadata.
3. Check for likely duplicates in both `Library/Papers/` and `Notes/`.
4. Normalize the filename into a stable, readable canonical form if confidence is sufficient.
5. Move the PDF into `Library/Papers/`.
6. Create or update the corresponding paper note in `Notes/`.
7. Verify that the note and PDF clearly point to the same source.

## Minimum Metadata

Capture what can be established with reasonable confidence:

- title
- author or authors
- year
- venue, publisher, or source type when clear
- DOI or stable URL when available

Do not fabricate precise metadata.

## Duplicate Check

Compare using practical signals such as:

- exact or near-exact title
- DOI
- first author plus year
- obviously similar normalized filenames

If a likely duplicate exists, prefer updating the existing note or resolving the conflict instead of creating parallel copies.

Use the `obsidian-cli` skill for vault-aware duplicate search and note retrieval when practical.

## Naming And Placement

- Prefer stable, human-readable filenames over importer noise.
- Keep `Library/Papers/` flat by default.
- Do not create topic folders unless the system changes deliberately later.

If metadata is incomplete, choose the least misleading readable name rather than inventing a rigid citation scheme.

## Paper Note

Create or update a corresponding note in `Notes/` that serves as the semantic interface to the paper.

Useful contents include:

- canonical title
- link or reference to the PDF
- minimal bibliographic metadata
- short summary or status when available
- links to related notes if they already exist

Do not require a heavy schema.

The resulting paper note should still satisfy the minimum processed-note metadata contract in `System/Rules/processed-note-metadata.md`.

If the resulting paper note is primarily non-English, include the minimum English retrieval bridge:

- `lang`
- English `aliases`
- English `search_terms`
- a short English `summary`

When integrating the paper note into navigation, use this fallback order:

1. existing topic hub or overview note
2. existing curated index section if the paper note is genuinely an entry point
3. bootstrap section in `Notes/Index.md` when no better navigation surface exists yet

Update `Notes/Index.md` only when the paper note clearly becomes a processed entry point, such as a key paper note or a topic anchor. Do not add every ingested paper to the index.

Bootstrap fallback is acceptable for ordinary paper notes during cold start or hub absence.

If the new or updated paper note likely needs later linking, overview integration, or broader sleep digestion, record one or more queue signals using `System/Skills/sleep/references/signal-writing.md`.

## When Not To Act

Defer or narrow the operation when:

- the PDF is not clearly a paper
- duplicate status is unresolved
- metadata is too uncertain to support a stable rename
- the move would create more churn than value

## Verification

After ingestion:

- confirm the PDF exists in `Library/Papers/`
- confirm the paper note exists or was updated in `Notes/`
- confirm the note and PDF still correspond after any rename
- confirm duplicate handling did not create a confusing parallel copy

## Related Skills

- `inbox-triage`
- `obsidian-cli`
- `path-change-policy`

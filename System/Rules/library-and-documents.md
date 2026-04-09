# Library And Documents

## Role Of `Library/Documents/`

`Library/Documents/` is the canonical storage location for source documents in this vault.

- It holds source documents, not their full semantic interpretation.
- Documents are first-class objects, not generic attachments.
- The folder should remain easy to scan and safe to manage from a cold start.

## Documents As First-Class Objects

Documents deserve explicit treatment because they often support multiple notes, claims, and future synthesis work.

- Keep the source file as a stable source object.
- Do not bury documents inside topic folders by default.
- Do not treat documents as incidental assets attached to a single note.

Papers remain one recognizable subtype of document, but not the top-level model.

## Relationship To Notes

Each ingested document should have a corresponding note in `Notes/`.

- the source file in `Library/Documents/` is the canonical source object
- the source note in `Notes/` is the semantic interface for summaries, links, quotes, claims, and follow-on thinking

The note and source file should stay clearly associated through names, links, and local metadata where helpful.

## Cold-Start Policy

The document library must be easy to use before a large corpus exists.

- Start with a flat document corpus.
- Prefer consistent filenames over early hierarchy.
- Avoid subtype-specific document folders until the volume and usage patterns clearly justify them.

## Default Storage Policy

At the beginning, `Library/Documents/` should remain flat.

- No default topic-based hierarchy
- No automatic subfolders by author, year, venue, or field
- No speculative taxonomies

If more structure is needed later, it should be introduced deliberately and incrementally.

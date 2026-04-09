# Processed Note Metadata

## Purpose

This rule defines the minimum metadata a note should have before it is treated as a processed note in `Notes/`.

The goal is future retrieval, not heavy schema.

See `System/Rules/processed-note-metadata-examples.md` for concrete note examples.

Minimum metadata should make a note:

- understandable at a glance
- retrievable later by agents and humans
- compatible with the vault's English-centric retrieval model

## Minimum Metadata For All Processed Notes

Every processed note in `Notes/` should have:

- `lang`: the note's primary language code
- `summary`: a short English summary that explains what the note is about

This is the smallest cross-cutting metadata contract for the knowledge layer.

## Why These Fields Are Required

`lang` is required because:

- agents need to know the note's primary language
- multilingual retrieval and later tooling should not depend on guesswork

`summary` is required because:

- a short English summary gives agents an immediate retrieval bridge
- it makes broad search and triage over many notes more reliable
- it helps future sleep passes decide where linking or integration work is likely useful

The summary should be concise and retrieval-oriented, not a full digest.

## Additional Metadata For Non-English Processed Notes

If the note's primary language is not English, it should also include:

- English `aliases`
- English `search_terms`

These fields improve cross-language retrieval in the shared English retrieval space.

## Optional Metadata

Additional metadata is allowed when useful, such as:

- tags
- source links
- timestamps
- topic-specific fields
- document-specific source metadata

Do not require optional metadata just to move a note out of `Inbox/`.

## When Metadata Must Exist

The minimum metadata should be present:

- before a note leaves `Inbox/` and enters `Notes/`
- when a non-English note is promoted into the knowledge layer
- when an existing note in `Notes/` is normalized into a properly processed note

## Summary Guidance

The English `summary` should usually:

- fit in one or two short sentences
- describe the note's main topic or function
- use retrieval-friendly wording rather than literary prose

Good examples:

- `Summary of the main argument for sparse autoencoders in mechanistic interpretability.`
- `Working note on knowledge graph linking patterns inside the vault.`

Avoid:

- long abstracts
- vague prose that does not help retrieval
- hidden assumptions that only make sense if the full note has already been read

## Verification

Before treating a note as processed, confirm:

- `lang` exists
- `summary` exists and is in English
- non-English notes also have English `aliases` and English `search_terms`
- the metadata improves retrieval rather than merely adding boilerplate

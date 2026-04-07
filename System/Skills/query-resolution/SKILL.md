---
name: query-resolution
description: Use this skill when answering questions over the vault by starting from note-layer retrieval, expanding through related notes and paper notes, and consulting raw PDFs only when the note layer is insufficient.
---

# Query Resolution

## When To Use

Use this skill when a user asks a question that should be answered from the contents of the vault rather than from general world knowledge.

## Inputs

- the user question
- English retrieval metadata on non-English durable notes when available
- `Notes/Index.md` when it exists
- access to vault search and note reading
- access to related paper notes and, when necessary, canonical PDFs

## Output

A grounded answer that:

- is supported by notes or sources actually present in the vault
- distinguishes direct support from inference
- states clearly when the vault is incomplete or ambiguous

## Procedure

1. If the user asks in a non-English language, translate the retrieval query into English before broad search.
2. Read `Notes/Index.md` first when it exists and the query is broad enough to benefit from a top-level map.
3. Search for directly relevant notes, paper notes, and summaries in English retrieval space.
4. Read the strongest initial hits.
5. Expand into English aliases, English `search_terms`, English summaries, linked notes, backlinks, and associated paper notes when useful.
6. Consult raw PDFs only when the note layer is insufficient or the question requires source verification.
7. Answer from the strongest available evidence in the vault.

Use the `obsidian-cli` skill when you need concrete CLI targeting, retrieval, or fallback behavior.

## Preferred Evidence Order

Prefer this order when available:

- durable summary notes
- paper notes in `Notes/`
- closely linked knowledge notes
- raw source files such as PDFs

Raw PDFs are a fallback source, not the default starting point.

## Expansion Rules

Expand conservatively:

- use the index as a navigation surface, not as proof that nothing else exists
- do not stop after failing to match the original query language; continue through English retrieval metadata
- read explicit links mentioned in the anchor note
- use outgoing links and backlinks when they materially improve retrieval
- inspect nearby summary or synthesis notes
- stop when additional notes stop adding evidence

Do not scan the whole vault if a bounded subset is enough.

## When Not To Escalate To PDFs

Stay in the note layer when:

- a durable summary already answers the question
- a paper note captures the needed claim accurately
- additional source reading would add little value

Escalate to a PDF only for missing details, source verification, or quote-level checks.

## Verification

Before finalizing:

- confirm the cited note or source actually supports the answer
- confirm the answer matches the current vault contents
- confirm cross-language misses were handled through English retrieval metadata when relevant
- avoid mixing unsupported outside knowledge into a vault-grounded response

## Related Skills

- `obsidian-cli`
- `paper-ingestion`

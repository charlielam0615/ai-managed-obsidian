# Sleep State

`System/State/sleep/` holds operational memory for bounded sleep work.

This tree is scaffolding for stateful workflows, not the semantic knowledge layer.

Use it for:

- queue signals under `queue/pending/` and `queue/deferred/`
- run records under `runs/`
- history entries under partitioned `history/YYYY/MM/`
- resolved signal records under `archive/resolved/YYYY/MM/`
- future operational tracking under `targets/` and `clusters/`

Do not treat this tree as the place where knowledge, links, summaries, or synthesis live.

Those belong in `Notes/`.

This tree should contain active runtime state only.
Reference examples live under `System/Skills/sleep/references/examples/`.

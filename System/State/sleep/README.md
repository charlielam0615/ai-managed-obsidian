# Sleep State

`System/State/sleep/` holds operational memory for bounded sleep work.

This tree is scaffolding for stateful workflows, not the semantic knowledge layer.

Use it for:

- queue signals under `queue/`
- run records under `runs/`
- history entries under `history/`
- future operational tracking under `targets/` and `clusters/`

Do not treat this tree as the place where knowledge, links, summaries, or synthesis live.

Those belong in `Notes/`.

The example records in this tree are references only. They are not active runtime state.

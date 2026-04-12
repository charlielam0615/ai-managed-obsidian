# Sleep

## Policy Purpose

Sleep is an allowed maintenance mode for bounded consolidation work in the vault.

It exists to help agents improve coherence over time without turning the vault into a constantly rewritten system.

## What Sleep May Do

At a policy level, sleep may:

- consolidate scattered understanding into better-integrated notes
- create or improve semantic scaffolding in `Notes/`
- connect related notes and sources
- process previously captured material incrementally

## Boundaries

Sleep is a bounded consolidation workflow.

- It should work in small passes.
- It should focus on integration quality rather than global rewrites.
- It should leave the vault more coherent than it found it.

## Non-Destructive Requirement

Sleep must be incremental and non-destructive.

- Do not rewrite the whole vault.
- Do not impose a speculative taxonomy.
- Do not perform broad reorganization without clear evidence that it is needed.
- Prefer additions, link improvements, summaries, and limited relocations over disruptive restructuring.

## Knowledge Layer Target

Sleep should create and strengthen integrated semantic scaffolding in the knowledge layer.

- The main output belongs in `Notes/`.
- The goal is better navigability, better synthesis, stronger linking, and better future digestion.
- `System/` should define policy, not absorb knowledge content.

## Implementation Detail

This file defines policy only.

Detailed sleep workflows live under `System/Skills/sleep/`, and bounded operational memory for sleep runs lives under `System/State/sleep/`.

Those implementation details must remain subordinate to this policy:

- note-layer outputs remain the source of semantic value
- sleep state remains operational memory only
- sleep continues to be bounded, incremental, and non-destructive

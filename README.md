# AI-Native Obsidian Knowledge Vault

A file-native, Git-friendly starting point for building an AI-native personal knowledge system on top of an Obsidian vault.

This repository is opinionated about a few things:

- the vault is the source of truth
- durable understanding should live in plain files
- organization should be incremental and non-destructive
- `Inbox/` is the only human intake point
- `Notes/` is the semantic knowledge layer
- `Library/Papers/` stores canonical PDF papers
- agent workflows should be explicit, portable, and reviewable

The repo currently focuses on the operating contract:

- `AGENTS.md` defines top-level agent routing and completion-evidence expectations
- `CLAUDE.md` defines project memory for Claude Code
- `System/Rules/` defines durable policy
- `System/Skills/` defines reusable operational workflows for agents

It is designed to work well under cold-start conditions, before embeddings, registries, or complex orchestration layers exist.

## Repository Layout

```text
AGENTS.md
CLAUDE.md
Inbox/
Notes/
Library/
  Papers/
System/
  README.md
  Rules/
  Skills/
```

### Top-level intent

- `AGENTS.md`: repo-wide agent entrypoint and workflow contract
- `CLAUDE.md`: project memory and task-routing guide for Claude Code
- `Inbox/`: single intake point for human-created new material
- `Notes/`: main Markdown knowledge layer
- `Library/Papers/`: canonical storage for PDF papers
- `System/`: operating contract for humans and agents

`Notes/Index.md` is the curated entry point into the note layer and should stay selective rather than exhaustive.

## What Is In Here

### Rules

`System/Rules/` currently includes:

- `content-index`
- `operating-model`
- `inbox-and-placement`
- `library-and-papers`
- `linking-and-naming`
- `obsidian-cli-first`
- `sleep`
- `safe-change-policy`
- `git-workflow`

These are policy files, not app code.

### Skills

`System/Skills/` currently includes:

- `inbox-triage`
- `paper-ingestion`
- `query-resolution`
- `path-change-policy`
- `obsidian-cli`
- `sleep`

These are packaged as Agent Skills directories with `SKILL.md` entrypoints.

## Design Principles

- Minimal folder structure by default
- Progressive disclosure instead of deep taxonomy
- Durable semantics in notes, links, and local metadata rather than hidden systems
- Bounded, reviewable changes
- Obsidian-aware operations when path or note identity matters
- Lean operational state, separate from the semantic layer

## Status

This repo currently defines the vault contract, core rules, and first-pass skills.

It does not yet fully implement:

- a populated `System/State/` runtime layer
- automation packaging or plugin distribution
- opinionated note templates beyond what the skills describe

That is intentional. The goal is to start with a clean, understandable base.

## Using The Vault In Obsidian

This repository is an Obsidian vault. Open the repository root as a vault in Obsidian.

For broad orientation, start with `Notes/Index.md` and expand from there through note links and related pages.

The workflow assumes:

- Obsidian is the primary note interface
- Obsidian CLI is preferred when it materially improves note-aware operations
- raw filesystem edits are still acceptable for narrow, safe changes

If you want CLI-based note operations, verify that `obsidian` works in your shell:

```sh
obsidian help
```

Obsidian's official CLI docs note that the desktop app must be running, and the CLI is intended for scripting, automation, and agentic workflows.

## Project-Local Skill Installation

This repository stores the canonical skills under `System/Skills/` because they are part of the vault's operating contract.

Different agent tools look for local skills in different places. The sections below show the cleanest project-local setup for each tool.

### Codex

The repo also includes a top-level `AGENTS.md` that routes common task types to the correct vault workflows and reporting expectations.

Codex officially supports Agent Skills and scans project-local skills from `.agents/skills/` as well as user-level and admin-level locations.

Important compatibility detail:

- this repo keeps the canonical skill definitions in `System/Skills/`
- Codex expects discovery from `.agents/skills/`
- Codex officially supports symlinked skill folders

The simplest project-local setup is to symlink the repo's canonical skills into `.agents/skills/`.

From the repository root:

```sh
mkdir -p .agents/skills

for dir in System/Skills/*; do
  [ -d "$dir" ] || continue
  name="$(basename "$dir")"
  ln -sfn "../../$dir" ".agents/skills/$name"
done
```

Then restart Codex if needed and verify:

```text
/skills
```

or explicitly invoke one:

```text
$sleep
$paper-ingestion
```

Notes:

- Codex reads skills from repo, user, admin, and built-in system locations.
- For reusable distribution beyond one repo, OpenAI recommends packaging skills as plugins rather than relying only on local folders.
- If you want a user-level install instead, use `~/.agents/skills/`.

### Claude Code

Claude Code does not use the exact same project-local skill discovery mechanism as Codex.

The official project-level mechanisms are:

- `CLAUDE.md` project memory
- `@path` imports inside `CLAUDE.md`
- project slash commands under `.claude/commands/`

Recommended approach for this repo:

1. Keep the canonical skill definitions in `System/Skills/`
2. Use the included lightweight project `CLAUDE.md`
3. Add project slash commands that tell Claude Code to read and use a specific skill on demand

Current `CLAUDE.md`:

```md
# Project Memory

See @README for repository overview.

# Skill Location

Reusable workflows for this vault live under `System/Skills/`.
When a task clearly matches one of those workflows, read the corresponding `SKILL.md` before acting.
```

Suggested project commands:

```sh
mkdir -p .claude/commands
```

Example `.claude/commands/sleep.md`:

```md
---
description: Run the repo's manual sleep workflow
---

Read `System/Skills/sleep/SKILL.md` and any files it references. Then carry out the requested bounded sleep pass.

Additional user context: $ARGUMENTS
```

Example `.claude/commands/inbox-triage.md`:

```md
---
description: Run the repo's inbox triage workflow
---

Read `System/Skills/inbox-triage/SKILL.md` and follow it for the current Inbox task.

Additional user context: $ARGUMENTS
```

Then use them inside Claude Code:

```text
/sleep work on the most central stale note cluster
/inbox-triage process the current inbox conservatively
```

Notes:

- `CLAUDE.md` is team-shared project memory.
- Anthropic documents `CLAUDE.local.md` as deprecated in favor of imports.
- Keep `CLAUDE.md` lean. Avoid importing every skill file directly unless you want all of them loaded into context eagerly.
- `CLAUDE.md` should route Claude toward `Notes/Index.md`, the matching skill in `System/Skills/`, and the relevant rules for structure-sensitive work.

### Other Tools

These skills follow the open Agent Skills directory format:

- one directory per skill
- a `SKILL.md` file with YAML frontmatter
- optional `references/`, `scripts/`, and `assets/`

That makes them portable to other tools that support the Agent Skills format directly, or adaptable through tool-specific imports, commands, or wrappers.

## State Layer

The `sleep` skill is explicitly designed to use `System/State/sleep/` for operational memory.

That state is intended to hold things like:

- per-target freshness
- cluster tracking
- run checkpoints
- audit history

It is intentionally not the semantic layer.

Durable understanding belongs in `Notes/`, not in hidden runtime state.

## Recommended Git Workflow

- keep commits small and coherent
- separate structure, content, and path changes when possible
- avoid broad vault churn
- prefer reviewable digests and synthesis over large rewrites

The repository includes rule files that codify this more precisely under `System/Rules/`.

## Why `sleep` Matters

The central idea in this repo is that future comprehension should get cheaper over time.

The `sleep` skill is the bounded manual consolidation pass that makes that happen. It creates progressive-disclosure layers in the vault itself so later humans and agents can understand dense material faster without relying on hidden memory.

## References

- OpenAI Academy: [Skills](https://academy.openai.com/public/resources/skills)
- OpenAI Developers: [Agent Skills for Codex](https://developers.openai.com/codex/skills)
- OpenAI Developers: [AGENTS.md for Codex](https://developers.openai.com/codex/guides/agents-md)
- Agent Skills open standard: [Specification](https://agentskills.io/specification)
- Anthropic: [Manage Claude Code memory](https://docs.anthropic.com/en/docs/claude-code/memory)
- Anthropic: [Claude Code slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- Obsidian: [CLI help](https://obsidian.md/help/cli)

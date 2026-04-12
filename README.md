# AI-Native Obsidian Knowledge Vault

A file-native, Git-friendly starting point for building an AI-native personal knowledge system on top of an Obsidian vault.

This repository is opinionated about a few things:

- the vault is the source of truth
- knowledge should live in plain files
- organization should be incremental and non-destructive
- `Inbox/` is the only human intake point
- `Notes/` is the semantic knowledge layer
- `Library/Papers/` stores canonical PDF papers
- agent workflows should be explicit, portable, and reviewable

The repo currently focuses on the operating contract:

- `AGENTS.md` defines top-level agent routing and completion-evidence expectations
- `CLAUDE.md` defines project memory for Claude Code
- `System/Rules/` defines the operating policy
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
- `language-and-cross-language-retrieval`
- `library-and-papers`
- `linking-and-naming`
- `note-processing-lifecycle`
- `processed-note-metadata`
- `notes-topic-folders`
- `obsidian-cli-first`
- `sleep`
- `safe-change-policy`
- `git-workflow`

These are policy files, not app code.

### Skills

`System/Skills/` currently includes:

- `inbox-triage`
- `document-ingestion`
- `query-resolution`
- `ai-writing`
- `path-change-policy`
- `obsidian-cli`
- `sleep`
- `wechat-article-download`

These are packaged as Agent Skills directories with `SKILL.md` entrypoints.

Notable addition:

- `ai-writing` helps agents outline, draft, revise, and polish substantial written pieces directly into the vault while respecting the `Inbox/` vs `Notes/` processing model and note metadata requirements.
- `wechat-article-download` captures `mp.weixin.qq.com` article URLs into `Inbox/` as readable Markdown notes, preserving source metadata and extracted article body for later triage.

## Design Principles

- Minimal folder structure by default
- Progressive disclosure instead of deep taxonomy
- Durable semantics in notes, links, and local metadata rather than hidden systems
- English-centric retrieval over multilingual note bodies
- Bounded, reviewable changes
- Obsidian-aware operations when path or note identity matters
- Lean operational state, separate from the semantic layer

## Note Lifecycle

The distinction between `Inbox/` and `Notes/` is processing status, not permanence.

- `Inbox/` contains notes and captures that are not yet fully processed.
- `Notes/` contains notes that are processed enough to participate in the knowledge layer.

For a note to leave `Inbox/` and enter `Notes/`, it should:

- be in the correct location
- have the required metadata
- be incorporated into the relevant index, hub, or navigation surface

Minimum metadata for processed notes is intentionally small:

- `lang`
- a short English `summary`

For non-English processed notes, also add English `aliases` and English `search_terms`.

Notes in `Notes/` remain open to future edits, linking, metadata improvement, relocation, and synthesis.

## Language Support

System-facing files stay in English.

Notes may be written in multiple languages. For reliable agent retrieval, non-English processed notes should carry a lightweight English bridge:

- `lang`
- English `aliases`
- English `search_terms`
- a short English `summary`

The intended operating model is that agents translate non-English queries into English for retrieval, search the vault through English metadata and normal note structure, and then answer in the user's language when appropriate.

Concrete examples for processed-note metadata live in [processed-note-metadata-examples.md](System/Rules/processed-note-metadata-examples.md).

## Status

This repo currently defines the vault contract, core rules, and first-pass skills.

It now includes an initial runtime state layer for bounded sleep maintenance under `System/State/sleep/`.

It does not yet fully implement:

- broader runtime state beyond the current `sleep` workflow
- automation packaging or plugin distribution
- opinionated note templates beyond what the skills describe

That is intentional. The goal is still to keep the system clean and understandable while adding workflow state only where it materially improves bounded re-runs.

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

## Quick Start

Use this when you want to turn the repository into your own working vault quickly.

1. Clone the repository and open it as an Obsidian vault.

   ```sh
   git clone <your-fork-or-copy-url> my-vault
   cd my-vault
   ```

2. Ask your agent to install the local project skills.

   This works for both Codex and Claude Code. A simple prompt is:

   ```text
   Install this repo's local skills so they are available in this project.
   ```

   For Codex, the expected result is that the project skills become discoverable from the repo. For Claude Code, the expected result is that project memory and any requested project commands point at the workflows under `System/Skills/`.

3. Re-initialize Git so your new repository tracks your notes and changes instead of this starter history.

   ```sh
   rm -rf .git
   git init
   git add .
   git commit -m "Initialize my knowledge vault"
   ```

4. Start adding notes.
   Put rough captures, clips, and drafts in `Inbox/`.

5. Ask the agent to digest your inbox.
   Do not manually add metadata or move notes into `Notes/`. The intended workflow is to put note-like material in `Inbox/` and let `$inbox-triage` process it into the knowledge layer.

6. Run a bounded `sleep` pass when you want the vault to become easier to navigate.
   Use `sleep` to add links, refresh summaries, improve local overviews, and strengthen the index without broad reorganization.

Helpful prompts:

```text
$inbox-triage process the current inbox conservatively
$ai-writing draft a note-backed article in Notes/ about <topic> for <audience>
$sleep work on the most central stale note cluster
```

## References

- OpenAI Academy: [Skills](https://academy.openai.com/public/resources/skills)
- OpenAI Developers: [Agent Skills for Codex](https://developers.openai.com/codex/skills)
- OpenAI Developers: [AGENTS.md for Codex](https://developers.openai.com/codex/guides/agents-md)
- Agent Skills open standard: [Specification](https://agentskills.io/specification)
- Anthropic: [Manage Claude Code memory](https://docs.anthropic.com/en/docs/claude-code/memory)
- Anthropic: [Claude Code slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- Obsidian: [CLI help](https://obsidian.md/help/cli)

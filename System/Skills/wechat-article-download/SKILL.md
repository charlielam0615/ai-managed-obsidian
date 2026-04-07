---
name: wechat-article-download
description: Use this skill when a user wants a WeChat article URL captured as content rather than just stored as a bare link, usually by downloading the article, extracting the readable body, and saving it into Inbox/ for later triage.
---

# WeChat Article Download

## When To Use

Use this skill when a user provides a `mp.weixin.qq.com` article URL and wants the article contents captured into the vault rather than merely bookmarked.

Typical cases:

- save this WeChat article to `Inbox/`
- download this WeChat post
- capture the content behind this WeChat link
- preserve a WeChat article for later digestion

## Inputs

- a WeChat article URL, usually under `https://mp.weixin.qq.com/s/...`
- the user's requested destination, usually `Inbox/`
- access to network retrieval when the current harness allows it

## Output

One of:

- a Markdown note in `Inbox/` containing the article title, source metadata, source URL, capture date, and extracted body text
- a minimal fallback note in `Inbox/` containing the source URL and a clear blocked-capture status when the article body cannot be retrieved safely
- a handoff to `inbox-triage` after the capture is complete, when the user explicitly asks for digestion or promotion

## Procedure

1. Confirm the URL is a WeChat article link.
2. Fetch the page content conservatively.
3. If the first fetch fails because of local proxy settings, DNS restrictions, or sandbox network limits, retry with the permissions required by the harness.
4. If WeChat serves an environment-verification page, retry with a mobile or WeChat-like user agent before giving up.
5. Extract the minimum useful metadata:
   - article title
   - source account when available
   - source URL
   - published date when recoverable
   - capture date
6. Extract the readable article body from the rendered HTML, typically from `#js_content`, and clean it into plain Markdown-friendly text.
7. Preserve image URLs as lightweight placeholders when downloading images is unnecessary or blocked.
8. Save the result into `Inbox/` as a single Markdown note.
9. If the user asks to digest or classify the article afterward, follow `inbox-triage` rather than forcing immediate placement during capture.

## Naming

Prefer a stable, readable inbox filename such as:

- `YYYY-MM-DD-wechat-<short-slug>.md`

Use the article title to form the slug when practical, but prefer a short readable fallback over a long noisy transliteration.

## Capture Note Contents

The inbox note should usually include:

- a clear title
- source account
- source URL
- published date when known
- captured date
- a short note about how the content was obtained when the extraction path was unusual
- the extracted article body

Do not add integrated synthesis, taxonomy, or cross-note linking during the capture step unless the user explicitly asks for digestion too.

## Obsidian And File Operations

If Obsidian-aware CLI creation is available and reliable, it may be used.

If not, a direct file write is acceptable here because creating a new capture note in `Inbox/` does not risk existing note identity or backlinks.

Avoid rename or move churn during the capture step.

## Failure Handling

If the article body cannot be recovered:

- preserve the source URL in `Inbox/`
- record the reason, such as verification wall, network block, or incomplete fetch
- avoid pretending the article was fully captured

Do not silently discard the request just because WeChat blocks the first retrieval attempt.

## Verification

After capture:

- confirm the inbox note exists
- confirm the source URL is present
- confirm title and metadata are not obviously corrupted
- confirm the extracted body is readable enough for later triage
- if a fallback note was created instead, confirm the blocked state is stated clearly

## Related Skills

- `inbox-triage`
- `obsidian-cli`

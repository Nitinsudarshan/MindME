
---
Four parallel surveys came back. Here's the consolidated picture, organized by category — nothing here is a recommendation to drop, just the landscape.

## 1. Local-first AI notetaking / knowledge base tools

|Tool|Stack|License|Status|
|---|---|---|---|
|**Reor**|Electron, LanceDB, Transformers.js embeddings, Ollama/llama.cpp|AGPL-3.0|**Archived Mar 2026** — closest architectural sibling to Mnemos (LanceDB + Ollama + local embeddings + note-linking), but development has stopped|
|**AnythingLLM**|React/Vite + Node/Express, pluggable vector DB (LanceDB default), ONNX MiniLM embeddings|MIT|~64.7k stars, very active, multi-tenant/workspace model, heavy provider-abstraction|
|**Onyx** (ex-Danswer)|Next.js + FastAPI, Vespa, Postgres/Redis/Celery|MIT (CE)|~31.6k stars, active, but enterprise/multi-service — 50+ connector permission-aware search, not single-user local-first|
|**PrivateGPT**|LlamaIndex/FastAPI, pluggable vector store|Apache-2.0|~57.4k stars, active — a "reference architecture" via dependency injection more than a polished app|
|**Obsidian plugins** — Smart Connections (client-side WASM, local-first, source-available license), Local GPT (minimal, MIT, no persistent index), Copilot for Obsidian (AGPL, has pivoted toward a hosted-agent cloud backend), Text Generator (MIT, prompt-templating)||||

**Notable finding**: two of the four active Obsidian AI plugins (Copilot, Text Generator) have drifted toward cloud/hosted models over the past year, while only Smart Connections and Local GPT stay strictly local — and both of those also stay deliberately smaller in scope. This is a real data point: **staying local-only and staying full-featured seems to be a genuine tension in this space**, not a solved problem elsewhere. Mnemos holding the line on both is a real differentiator, not a redundant one.

## 2. Voice dictation & text-injection mechanisms

|Tool|Stack|Injection method|License/status|
|---|---|---|---|
|**Whispering**|Tauri + Svelte5|Clipboard + simulated paste|MIT, **archived**, folded into EpicenterHQ/epicenter|
|**Buzz**|Python + PyQt|N/A (transcription viewer, not live dictation)|MIT, ~21k stars, active|
|**VoiceInk**|Native Swift/SwiftUI, macOS-only|**Accessibility API direct text insertion**, with fallback to clipboard+CGEvent paste, then char-by-char CGEvent typing|GPLv3, ~5.9k stars, active|
|**Handy**|Tauri + Rust + React/TS|`enigo` (same as Mnemos) + clipboard paste; Linux via xdotool/wtype|MIT, ~29.6k stars, very active|
|**espanso**|Rust, modular|Simulated key events (OS-native APIs) or clipboard+paste, configurable|GPL-3.0, ~14.3k stars, active|

**Two things worth keeping open**: (1) **VoiceInk's graduated injection strategy** (try OS accessibility API insertion first, fall back to paste, fall back to char-by-char) is a genuinely more reliable pattern than pure keystroke simulation — Windows has an equivalent (UI Automation API) that Mnemos's `enigo`-only approach doesn't currently try. (2) **Handy is almost exactly Mnemos's architecture** (Tauri+Rust+enigo+local Whisper) and is both bigger and more active — worth a closer look at its `transcribe-rs`/`transcribe-cpp` bindings if faster-whisper's performance ever becomes a bottleneck, per the earlier OpenWhispr discussion.

## 3. Continuous context/recall capture (Step 9 relevant)

Context: Rewind.ai was acquired by Meta and shut down in Dec 2025, which triggered a wave of open-source alternatives in the last ~8 months.

|Tool|Stack|Storage|License/status|
|---|---|---|---|
|**Screenpipe**|Tauri + Rust|100% local (SQLite + JPEGs), local REST API|**Switched from MIT to a proprietary source-available license in 2026** (free personal use only) — ~21k stars, most mature, now a YC company|
|**OpenRecall**|Python, local web UI|Local SQLite, optional encryption|AGPL-3.0, ~2.9k stars, active|
|**Windrecorder**|Python/Streamlit|Local, ffmpeg-compressed|GPL-2.0, ~3.9k stars, oldest (since 2023), active|
|Retrace, RewindOS|Swift / Rust-Tauri|Local|MIT / AGPL, both small and early-stage|

**Takeaway**: this category isn't a huge technical lift — event-driven screenshot/audio capture, OCR or Whisper, local SQLite + embeddings for recall. The hard part is platform capture-permission handling and storage/retention, not the indexing logic. Screenpipe's license change is a useful cautionary data point if this space is ever revisited: even "local-first" projects in this category are moving toward commercial licensing once they mature, which is either a market signal (this is valuable enough to monetize) or a caution (staying open/local-only long-term takes deliberate resistance to that pull) — worth remembering if Step 9 ever gets scoped for real.

## 4. MCP ecosystem (Step 6 relevant)

- **Official `modelcontextprotocol/servers` repo has narrowed its scope** — Calendar/Gmail/Slack reference servers were moved to an archived repo; Anthropic isn't maintaining those as references anymore. Step 6's Calendar/Email connectors will have to lean on **community servers**, which the survey found meaningfully fragmented: `nspady/google-calendar-mcp` looks like the healthiest Calendar option; Gmail servers (`GongRzhe/Gmail-MCP-Server` and forks) show mixed/uncertain maintenance. **This is a real risk to flag for the PRD** — budget time to vet and pin a specific fork rather than assuming an official-quality server exists.
- **WhatsApp MCP**: `lharries/whatsapp-mcp` confirmed as still the most-referenced option but reportedly stale since ~April 2025, with `verygoodplugins/whatsapp-mcp` cited as an active fork (unverified in depth). No official Meta MCP server exists — this matches what was already assumed in the original brief.
- **New idea surfaced, not previously on the roadmap**: exposing Mnemos's own vault search _as_ an MCP server (not just consuming others') turns out to be an established pattern — Obsidian already has community plugins doing exactly this (an "MCP Server" plugin exposing read/write vault tools with bearer-token auth, and a separate Fastify-based "Vault as MCP" plugin). This would let other MCP clients (Claude Desktop, etc.) query your vault through Mnemos, rather than Mnemos only ever being the consumer. Flagging this as a real, validated option to consider for the roadmap — not proposing it definitively, since you asked me not to scrap or pre-filter ideas at this stage.

---
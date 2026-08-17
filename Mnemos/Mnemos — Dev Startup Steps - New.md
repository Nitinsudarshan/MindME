
---
## 0. Prerequisites (one-time installs)

Install these first, in this order, since a couple have dependencies on the others:

1. **Python 3.11+** — from [python.org](https://python.org) or the Microsoft Store. **Important:** afterward, go to Settings → Apps → Advanced app settings → App execution aliases, and turn off the `python.exe`/`python3.exe` aliases — they conflict with a real Python install and are a known gotcha in this build.
2. **Node.js + npm** — LTS from [nodejs.org](https://nodejs.org).
3. **Rust**, via `winget install Rustlang.Rustup`, then **close and reopen your terminal** (PATH won't refresh in an already-open one).
4. **Visual Studio Build Tools** — "Desktop development with C++" workload (needed for `link.exe`, which Tauri's Rust build requires). Close/reopen the terminal again afterward.
5. **Ollama** — from [ollama.com](https://ollama.com).

Verify each: `python --version`, `node --version`, `npm --version`, `cargo --version`, `ollama --version`.

## 1. Get the code

cd D:\Projects
git clone https://github.com/Nitinsudarshan/Mnemos.git
cd Mnemos

(If you already have a clone, just `git pull origin main` instead.)

## 2. Python backend setup

python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt

This installs everything, including the Step 6 connector libraries (`mcp`, Google API client) — you can ignore those if you're not using Notion/Google Docs yet.

## 3. Initialize the vault

python -m backend.cli init

Creates `vault/Notes/`, `vault/Meetings/`, `vault/Research/`, `vault/Reference/`, `vault/Journal/`. If you have existing notes, drop them in and skip this.

## 4. Ollama (for `ask` / `voice-ask`)

ollama serve

In another terminal:

ollama pull gemma4:latest

(That's the model actually configured as the default in [`backend/llm.py`](https://github.com/Nitinsudarshan/Mnemos/blob/claude/mnemos-project-handoff-oyrdpq/backend/llm.py). If you'd rather use a different model, e.g. `llama3.1`, pull that instead and set `$env:MNEMOS_LLM_MODEL="llama3.1"` before starting the backend.)

## 5. Piper (TTS) voice model

Still with the venv active:

python -m piper.download_voices en_US-lessac-medium --download-dir ./piper-voices

This produces `piper-voices\en_US-lessac-medium.onnx` — you'll point an env var at it below.

## 6. First run of the CLI (sanity check before the full app)

python -m backend.cli reindex
python -m backend.cli search "test"

The first `reindex` downloads the embedding model (~80MB) — needs internet once. If `search` runs without error, retrieval is working.

## 7. Everyday dev startup — two terminals

**Terminal A — backend:**

cd D:\Projects\Mnemos
.venv\Scripts\Activate.ps1
$env:MNEMOS_PIPER_MODEL = "D:\Projects\Mnemos\piper-voices\en_US-lessac-medium.onnx"
uvicorn backend.server:app --host 127.0.0.1 --port 8765

`MNEMOS_PIPER_MODEL` is the one required, no-default, machine-specific env var — and it's **session-scoped**, so you have to re-set it every time you open a fresh terminal (the single most common recurring mistake in this build). Everything else (CORS origins, LLM model/URL) already has a working default baked in.

Check it's alive by opening `http://127.0.0.1:8765/health` in a browser, or `http://127.0.0.1:8765/docs` for the full Swagger UI.

**Terminal B — Tauri shell (first time will also `npm install`):**

cd D:\Projects\Mnemos\shell
npm install
npm run tauri dev

The first Rust build will take a while (compiling Tauri + all its deps). If it fails with `linker` link.exe `not found`, that means the MSVC Build Tools step above didn't take — reinstall and reopen the terminal.

A native window should open: chat box, 🎙 Record button, and a status line showing "Backend: connected". Global hotkeys work anywhere on your machine once the app is running:

- **Ctrl+Shift+Space** — show/hide the window 
- **Ctrl+Space** (hold, release to send) — dictate into whatever field has focus (this is the fix I just pushed — genuinely not yet tested on real hardware, so it's worth being your first thing to try)

## 8. Optional — MCP connectors (Step 6, still unverified end-to-end)

Only if you want to try Notion/Google Docs search right now:

# Notion — needs a token from completing Notion's OAuth flow once (e.g. `npx mcp-remote https://mcp.notion.com/mcp`)
$env:MNEMOS_NOTION_TOKEN = "<token>"
python -m backend.cli notion-search "roadmap notes"

# Google Docs — needs an OAuth client secret JSON from Google Cloud Console (Desktop app type)
$env:MNEMOS_GOOGLE_CREDENTIALS = "D:\Projects\Mnemos\client_secret.json"
python -m backend.cli google-docs-search "quarterly plan"

---

If anything errors out, the `HANDOFF.md` file in the repo root has a "Windows-specific setup gotchas" section covering exactly the issues people hit here before (Ollama transient crashes, wrong audio output device, the Tauri dev port landing on 1430 not 1420, etc.) — worth checking there first before treating it as a new bug.
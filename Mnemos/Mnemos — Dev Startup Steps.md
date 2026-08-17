---

---
---
#mnemos 
Two terminals, in order. Requires: `ollama serve` also running separately if you plan to use `/ask` or `/voice-ask`.

## Terminal A — Backend

```powershell
cd D:\Projects\Mnemos
.venv\Scripts\Activate.ps1
uvicorn backend.server:app --host 127.0.0.1 --port 8765
```

Leave running. Confirm: `Uvicorn running on http://127.0.0.1:8765`

(No `$env:MNEMOS_CORS_ORIGINS` needed anymore — the Tauri dev port `127.0.0.1:1430` is now baked into `server.py`'s default.)

## Terminal B — Tauri shell

```powershell
cd D:\Projects\Mnemos\shell
npm run tauri dev
```

Wait for `Finished ... target(s)` and the window to open.

## Optional — Ollama (only needed for /ask, /voice-ask)

```powershell
ollama serve
```

If you get `bind: Only one usage of each socket address...`, it's already running somewhere — no action needed.

## Sanity check

In the Mnemos window, click "Check backend" → should show **"Backend says: ok"** in green. If red, check Terminal A is still running and check the webview console (F12 → Console) for the actual error.
#!/usr/bin/env bash
# One-time setup per clone: point git at the tracked hooks directory so the
# vault-lint pre-commit hook actually runs. See
# Rules/10 - Agent and AI Assistant Protocol.md for why this is the "soft"
# local enforcement layer, with .github/workflows/vault-lint.yml as the
# backstop that runs regardless of whether this was ever done.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

git config core.hooksPath .githooks
chmod +x .githooks/pre-commit scripts/lint_vault.py

echo "core.hooksPath set to .githooks — vault lint now runs before every commit in this clone."

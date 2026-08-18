#!/usr/bin/env python3
"""Validate vault notes against Rules/03 - Frontmatter and Metadata.md and
Rules/02 - File Naming.md.

Usage:
    lint_vault.py                # lint every tracked .md file in the vault
    lint_vault.py FILE [FILE...] # lint only the given files (used by the
                                  # pre-commit hook and the CI workflow, which
                                  # pass only the changed/staged .md files)

Exits non-zero if any violation is found.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Folders whose .md files intentionally don't follow the frontmatter schema —
# see "Rules/03 - Frontmatter and Metadata.md" section 5.
EXEMPT_PREFIXES = (
    "Clippings/",
    "06-Templates/",
    ".obsidian/",
    "Active Projects/.agents/",
    "Active Projects/Rules/",
)

# Same exemption, but pattern-based for the per-app .agents/Rules/AGENTS.md
# sets PDDB Prompt Template seeds under App Ideas/<AppName>/ — one entry
# covers every current and future app, not just a hardcoded name.
EXEMPT_PATTERNS = (
    re.compile(r"^App Ideas/[^/]+/\.agents/"),
    re.compile(r"^App Ideas/[^/]+/Rules/"),
    re.compile(r"^App Ideas/[^/]+/AGENTS\.md$"),
)

# Repo-meta files, not vault notes — no frontmatter schema applies to these.
EXEMPT_FILES = {"CLAUDE.md", "AGENTS.md", "README.md"}

ALLOWED_TYPES = {"moc", "project", "area", "resource", "daily", "fleeting"}
ALLOWED_STATUS = {"seedling", "growing", "evergreen"}
REQUIRED_KEYS = ("title", "tags", "type", "status", "created", "updated")
MAX_TAGS = 7

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BAD_NAME_RE = re.compile(r"^(untitled|new note|notes?\d*)$", re.IGNORECASE)
FORBIDDEN_CHARS = set(':*?"<>|\\')


def tracked_md_files():
    out = subprocess.run(
        ["git", "ls-files", "*.md"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return [ROOT / p for p in out.stdout.splitlines() if p]


def parse_frontmatter(text):
    """Minimal parser for the flat-scalar + simple-list YAML this vault uses.
    Returns None if there's no frontmatter block at all."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")

    data = {}
    key = None
    for line in block.splitlines():
        list_item = re.match(r"^\s*-\s*(.*)$", line)
        if list_item and key:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(list_item.group(1).strip().strip("\"'"))
            continue

        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip().strip("\"'") for v in inner.split(",") if v.strip()]
        elif val == "":
            data[key] = []
        else:
            data[key] = val.strip("\"'")
    return data


def lint_file(path):
    errors = []
    rel = path.relative_to(ROOT).as_posix()

    if (
        rel in EXEMPT_FILES
        or any(rel.startswith(p) for p in EXEMPT_PREFIXES)
        or any(p.match(rel) for p in EXEMPT_PATTERNS)
    ):
        return errors

    stem = path.stem
    if BAD_NAME_RE.match(stem.strip()):
        errors.append(f"{rel}: placeholder-looking filename ('{stem}') — see Rules/02 - File Naming.md")
    if any(c in stem for c in FORBIDDEN_CHARS) or stem != stem.rstrip(" ."):
        errors.append(f"{rel}: filename has cross-platform-unsafe characters or trailing space/period — see Rules/02 - File Naming.md")

    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        errors.append(f"{rel}: missing YAML frontmatter block — see Rules/03 - Frontmatter and Metadata.md")
        return errors

    for key in REQUIRED_KEYS:
        if key not in fm or fm[key] in ("", None, []):
            errors.append(f"{rel}: frontmatter missing required field '{key}' — see Rules/03 - Frontmatter and Metadata.md")

    if fm.get("type") and fm["type"] not in ALLOWED_TYPES:
        errors.append(f"{rel}: type '{fm['type']}' not one of {sorted(ALLOWED_TYPES)} — see Rules/03 - Frontmatter and Metadata.md")

    if fm.get("status") and fm["status"] not in ALLOWED_STATUS:
        errors.append(f"{rel}: status '{fm['status']}' not one of {sorted(ALLOWED_STATUS)} — see Rules/03 - Frontmatter and Metadata.md")

    tags = fm.get("tags")
    if isinstance(tags, list):
        if len(tags) == 0:
            errors.append(f"{rel}: needs at least 1 tag — see Rules/04 - Tagging.md")
        elif len(tags) > MAX_TAGS:
            errors.append(f"{rel}: {len(tags)} tags exceeds the {MAX_TAGS}-tag max — see Rules/04 - Tagging.md")

    for dkey in ("created", "updated"):
        v = fm.get(dkey)
        if v and not DATE_RE.match(v):
            errors.append(f"{rel}: '{dkey}: {v}' is not YYYY-MM-DD — see Rules/03 - Frontmatter and Metadata.md")

    return errors


def main(argv):
    if argv:
        paths = [Path(p).resolve() for p in argv]
    else:
        paths = tracked_md_files()
    paths = [p for p in paths if p.suffix == ".md" and p.exists()]

    all_errors = []
    for p in paths:
        all_errors.extend(lint_file(p))

    if all_errors:
        print("Vault lint failed:\n")
        for e in all_errors:
            print(f"  - {e}")
        print(f"\n{len(all_errors)} issue(s) across {len(paths)} file(s) checked.")
        print("Fix the note(s) above — see Rules/00 - Rules Index.md for the full rule set.")
        return 1

    print(f"Vault lint passed ({len(paths)} file(s) checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

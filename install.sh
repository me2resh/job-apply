#!/usr/bin/env bash
# Install Job Apply into an agent's skills directory (for agents that do not use Claude Code plugins).
# Claude Code users: /plugin marketplace add me2resh/job-apply, then /plugin install job-apply@job-apply
# Usage: ./install.sh [claude|codex|all|<directory>]
# Any agent that supports the Agent Skills format (a folder with SKILL.md) can use the same folder:
# point it at the folder, or copy the folder into that agent's skills directory.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TARGET="${1:-all}"
copy() { mkdir -p "$1"; rm -rf "$1/job-apply"; mkdir -p "$1/job-apply"; cp -R "$HERE/skills/job-apply/." "$1/job-apply/"; echo "installed: $1/job-apply"; }
if [ "$TARGET" != "claude" ] && [ "$TARGET" != "codex" ] && [ "$TARGET" != "all" ]; then
  case "$TARGET" in
    */*|.|..|~*) ;;   # looks like a path
    *) echo "Unknown target '$TARGET'. Usage: ./install.sh [claude|codex|all|/path/to/agent/skills]" >&2; exit 2 ;;
  esac
  [ -d "$(dirname "$TARGET")" ] || { echo "Parent folder of '$TARGET' does not exist." >&2; exit 2; }
fi
case "$TARGET" in
  claude) copy "$HOME/.claude/skills" ;;
  codex)  copy "$HOME/.codex/skills" ;;
  all)    copy "$HOME/.claude/skills"; copy "$HOME/.codex/skills" ;;
  *)      copy "$TARGET" ;;
esac
cat <<'MSG'
Cursor: copy .cursor/rules/job-apply.mdc into your project's .cursor/rules/ (or the whole folder into ~/.cursor/skills/ if your version supports skills).
Copilot: copy .github/copilot-instructions.md into your project, or append its text to yours.
Other agents: add the AGENTS.md text to your agent's instructions file and keep skills/job-apply/ where the agent can read it.
MSG

set -eo pipefail

# Check if terminal supports colors
if [ -t 1 ] && command -v tput >/dev/null 2>&1 && tput colors >/dev/null 2>&1; then
    COLOR_GREEN=$(tput setaf 2)
    COLOR_BLUE=$(tput setaf 4)
    COLOR_RED=$(tput setaf 1)
    COLOR_NC=$(tput sgr0)
else
    COLOR_GREEN=""
    COLOR_BLUE=""
    COLOR_RED=""
    COLOR_NC=""
fi

cd "$(dirname "$0")/../.."

echo "${COLOR_BLUE}Start Ruff Auto Fix${COLOR_NC}"
uv run ruff check . --fix || true
echo "${COLOR_GREEN}Auto-fix Done${COLOR_NC}"

echo "${COLOR_BLUE}Check remaining issues${COLOR_NC}"
if ! uv run ruff check .; then
  echo ""
  echo "${COLOR_RED}✖ Ruff found issues that could NOT be auto-fixed.${COLOR_NC}"
  echo "${COLOR_RED}→ Please fix the issues above manually and re-run the command.${COLOR_NC}"
  exit 1
fi

echo "${COLOR_BLUE}Start Formatting${COLOR_NC}"
uv run ruff format .

echo "${COLOR_GREEN}Code formatting successfully!${COLOR_NC}"

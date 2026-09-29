"""Check local skill links and coverage of the user-supplied website list."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "SKILL.md"
CATALOG = ROOT / "references" / "source-research.md"
WEBSITES = ROOT / "Websites.txt"
if not WEBSITES.is_file():
    WEBSITES = ROOT.parent / "Websites.txt"

errors: list[str] = []

if not ENTRY.is_file():
    errors.append("missing SKILL.md")
if not CATALOG.is_file():
    errors.append("missing source-research.md")

markdown_files = [ENTRY, *sorted((ROOT / "references").glob("*.md"))]
for file in markdown_files:
    if not file.is_file():
        continue
    content = file.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local_target = target.split("#", 1)[0]
        if local_target and not (file.parent / local_target).is_file():
            errors.append(f"broken link in {file.relative_to(ROOT)}: {target}")

if ENTRY.is_file():
    content = ENTRY.read_text(encoding="utf-8")
    if not content.startswith("---\n") or "\nname: interface-forge\n" not in content:
        errors.append("invalid or missing skill frontmatter")
    if "\ndescription:" not in content:
        errors.append("missing skill description")

if WEBSITES.is_file() and CATALOG.is_file():
    supplied = WEBSITES.read_text(encoding="utf-8")
    catalog = CATALOG.read_text(encoding="utf-8")
    urls = {url.rstrip(".,") for url in re.findall(r"https?://[^\s]+", supplied)}
    for url in sorted(urls):
        if url not in catalog:
            errors.append(f"website missing from source catalog: {url}")
    if "https://motion.dev/" not in catalog:
        errors.append("Motion.dev is not normalized in the source catalog")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"Interface Forge check passed: {len(markdown_files)} Markdown files; source catalog covered.")

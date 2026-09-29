"""Check Interface Forge reference integrity."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
links = re.findall(r"\]\((references/[^)]+\.md)\)", text)
errors = [f"missing reference: {p}" for p in links if not (ROOT / p).exists()]
errors += [f"missing marker: {m}" for m in ("name: interface-forge", "description:", "# Interface Forge") if m not in text]
if errors:
    print("\n".join(errors)); sys.exit(1)
print(f"Interface Forge self-check passed ({len(set(links))} routed references).")


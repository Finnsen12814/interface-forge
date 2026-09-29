# Interface Forge

Website-first UI/UX for Codex and Claude Code. The skill researches, specifies, implements, redesigns, and audits websites, desktop apps, and mobile apps. New visual elements come exclusively from the websites in the user's `Websites.txt`, transcribed into `references/source-research.md` so the installed skill is self-contained. Apple Developer Human Interface Guidelines guide usability and design decisions.

Before importing any external element, the agent proposes its **exact element link**, intended use, and adaptation, then waits for the user's approval. The detailed process is in `references/sourcing-and-approval.md`. Galleries may inform an original direction but do not grant rights to their featured sites' assets.

## Install

Copy the `interface-forge` folder to one or both locations:

```text
Codex:  ~/.codex/skills/interface-forge
Claude: ~/.claude/skills/interface-forge
```

Reload the client, then invoke `$interface-forge` or request UI/UX design, implementation, or review work.

`SKILL.md` routes the workflow; `references/` contains the source catalog, approval process, Apple HIG checklist, design and UX playbooks, web/mobile/desktop production guidance, and quality gates. `scripts/check_skill.py` checks reference integrity; `agents/openai.yaml` supplies Codex metadata. No third-party visual assets are bundled.

## License

MIT. Third-party sites, code, assets, and trademarks retain their own terms.

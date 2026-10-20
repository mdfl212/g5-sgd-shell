# GitHub Copilot instructions — G5 SGD Shell

- Read `SKILL.md`, `theme.json`, and `docs/ARCHITECTURE.md` before changing generation behavior.
- Preserve the locked first-occurrence sequence: cover → case → questions → answers → visuals → takeaways → references → thank-you. Multiple answer slides are allowed.
- Keep MD201–MD207 palette values in `theme.json`; do not duplicate them as independent hard-coded configuration elsewhere.
- Use Cambria, 10 × 5.625-inch slides, and the provided CSU SoM shield asset unless the user explicitly changes the shell.
- Keep clinical claims traceable to supplied source material. Never invent patient facts or references.
- Prefer editable PowerPoint shapes and tables. Preserve figure aspect ratios when figure placement is implemented.
- Draw flowchart arrows after nodes so arrows remain visible above the boxes.
- Run `python scripts/check_package.py`, `python -m unittest discover -s tests -v`, `python scripts/build_deck.py`, and `python scripts/validate_deck.py dist/g5-demo-deck.pptx --outline examples/demo-outline.json` after relevant changes.
- Do not commit real patient data, local case files, or generated case-specific decks.
- Document limitations honestly. Passing structural validation is not proof of visual quality, clinical correctness, or reference accuracy.

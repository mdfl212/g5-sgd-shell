# G5 SGD Shell

A configurable, source-grounded PowerPoint-generation workflow for Group 5 small-group discussions at Caraga State University School of Medicine (CSU-SoM), covering MD201–MD207.

## Project status

The starter implementation is developed locally and includes a Python PowerPoint renderer, subject palettes, an outline schema, a demo outline, validation scripts, tests, and GitHub Actions CI. This remote repository is currently being initialized; the complete starter package and binary design assets still need to be published here.

## Design constraints

- Preserve the locked eight-step SGD slide spine: Cover; Case/Snapshot; Guide Questions overview; Answer blocks; Tables/Flowcharts; Summary & Take-aways; References; Thank-you.
- Keep the CSU-SoM shield, school header, course code, subject-color bars, topic footer, and page number on every slide.
- Use Cambria typography and visual-first, editable PowerPoint elements.
- Preserve source fidelity, figure aspect ratios, case boundaries, and Vancouver-style references.
- Treat clinical correctness, citation truth, text overflow, and visual quality as separate review tasks; successful programmatic validation alone is not a clinical or presentation-quality sign-off.

## Local setup

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_package.py
python -m unittest discover -s tests -v
python scripts/build_deck.py
python scripts/validate_deck.py dist/g5-demo-deck.pptx --outline examples/demo-outline.json
```

See `SKILL.md`, `CHATGPT_INSTRUCTIONS.md`, and `docs/ARCHITECTURE.md` for the authoring contract and implementation notes.

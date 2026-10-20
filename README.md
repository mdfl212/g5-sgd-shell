# G5 SGD Shell

A reusable, source-first workflow for building consistent Group 5 Small Group Discussion (SGD) PowerPoint decks for Caraga State University School of Medicine (CSU SoM), modules MD201–MD207.

> **Status:** Early prototype. The source code, theme configuration, outline schema, example outline, tests, documentation, and GitHub Actions workflow are published. The original PowerPoint template and CSU shield are binary assets that are still pending upload. Until those assets are added under `assets/`, generated decks will omit the shield and the template-inspection command cannot run.

## Goals

- Enforce the locked eight-step narrative spine.
- Apply the MD201–MD207 color palette and consistent CSU SoM branding.
- Keep slides editable in PowerPoint.
- Preserve clinical/source fidelity and cite references in Vancouver style.
- Validate slide geometry and outline structure before delivery.
- Make the workflow usable from GitHub Copilot / VS Code and other agents that support skill files.

## Repository contents

```text
.
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/ci.yml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── EXTERNAL_SKILLS.md
│   └── ROADMAP.md
├── examples/demo-outline.json
├── schemas/outline.schema.json
├── scripts/
│   ├── build_deck.py
│   ├── inspect_template.py
│   ├── validate_deck.py
│   └── check_package.py
├── tests/test_outline_schema.py
├── theme.json
├── CHATGPT_INSTRUCTIONS.md
└── SKILL.md
```

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/check_package.py
python -m unittest discover -s tests -v
python scripts/build_deck.py
python scripts/validate_deck.py dist/g5-demo-deck.pptx --outline examples/demo-outline.json
```

To inspect the supplied PowerPoint after adding it to `assets/G5_SGD_Shell_Template_MD201-MD207.pptx`, run:

```bash
python scripts/inspect_template.py
```

## Locked slide spine

1. Cover
2. Case / Snapshot
3. Guide Questions overview
4. Answer blocks (one per question)
5. Tables / Flowcharts
6. Summary & Take-aways
7. References
8. Thank-you

Additional slides may live within these steps but must not introduce new top-level sections or reorder the spine.

## Development principles

- Source material is authoritative for the case; distinguish sourced facts from clinical context added for explanation.
- Do not invent patient details, lab values, citations, or references.
- Prefer editable PowerPoint shapes, tables, and charts over full-slide screenshots.
- Preserve the original aspect ratio of source figures.
- Keep code, skill instructions, and theme metadata synchronized.
- Run the package check and tests before sharing generated decks.
- Use synthetic examples in the public repository and keep identifiable patient information out of Git.

## Validation limits

The validator checks PowerPoint integrity, slide dimensions, outline step order, and shape bounds. It does not prove text fits, figures are preserved, references are accurate, or clinical content is correct. Treat these as separate review gates.

## Pending upload

The complete local starter ZIP includes the original shell PPTX and CSU SoM shield image. These binary files are not yet present in this GitHub repository. Add the two files to `assets/` before treating the repository as a complete branded template package.

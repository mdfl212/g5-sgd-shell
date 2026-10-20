# G5 SGD Shell

A reusable, source-first workflow for building consistent Group 5 Small Group Discussion (SGD) PowerPoint decks for Caraga State University School of Medicine (CSU SoM), modules MD201–MD207.

> **Status:** Early prototype. A basic editable PowerPoint renderer, outline checks, structural deck validator, theme configuration, and template inspector are implemented. Full visual QA, text-overflow detection, figure insertion, and clinical-source validation remain planned.

## Goals

- Enforce the locked eight-step narrative spine.
- Apply the MD201–MD207 color palette and consistent CSU SoM branding.
- Keep slides editable in PowerPoint.
- Preserve clinical/source fidelity and cite references in Vancouver style.
- Validate slide geometry, image aspect ratios, content coverage, and visual rendering before delivery.
- Make the workflow usable from GitHub Copilot / VS Code and other agents that support skill files.

## Repository contents

```text
.
├── assets/
│   ├── G5_SGD_Shell_Template_MD201-MD207.pptx
│   └── csu_som_shield.png
├── docs/
│   ├── ARCHITECTURE.md
│   ├── EXTERNAL_SKILLS.md
│   └── ROADMAP.md
├── references/
├── schemas/
│   └── outline.schema.json
├── examples/
│   └── demo-outline.json
├── scripts/
│   ├── build_deck.py
│   ├── inspect_template.py
│   ├── validate_deck.py
│   └── check_package.py
├── tests/
├── theme.json
├── CHATGPT_INSTRUCTIONS.md
├── SKILL.md
└── README.md
```

## Quick start

1. Open the repository in VS Code.
2. Open `SKILL.md` and `CHATGPT_INSTRUCTIONS.md` to review the behavioral and output constraints.
3. Place the case vignette, guide questions, and source materials in a working folder. Do not commit identifiable patient information or copyrighted textbooks/PDFs without permission.
4. Choose the subject code (MD201–MD207), confirm the guide questions and Group 5 roster, and generate/rebuild the deck.
5. Install the small Python dependency set and build the included non-clinical demo deck:

   ```bash
   python -m pip install -r requirements.txt
   python scripts/check_package.py
   python -m unittest discover -s tests -v
   python scripts/build_deck.py
   python scripts/validate_deck.py dist/g5-demo-deck.pptx --outline examples/demo-outline.json
   ```

6. Inspect the source template structure when it changes:

   ```bash
   python scripts/inspect_template.py
   ```

The renderer is an early prototype. The validator checks basic PPTX integrity, slide dimensions, outline step order, and shape bounds; it does not prove text fits or that clinical claims and references are correct.

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

A passing structural validator is not a substitute for visual inspection, checking text overflow, verifying references, or reviewing clinical content against source material. Treat these as separate quality gates.

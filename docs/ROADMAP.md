# Roadmap

## Phase 0 — Repository baseline
- [x] Add skill instructions and ChatGPT instructions.
- [x] Define the locked spine, palette, source-fidelity rules, and development plan.
- [x] Add a starter package-integrity check.

## Phase 1 — Inspect and formalize the shell
- [x] Inspect template layouts, masters, placeholders, and slide inventory.
- [x] Confirm dimensions and reusable layout names.
- [x] Create `theme.json` for MD201–MD207.
- [x] Emit a detailed template shape/text inventory locally.

## Phase 2 — Structured outline and renderer
- [x] Define an outline schema and example.
- [x] Implement a Python python-pptx renderer using editable shapes and text.
- [x] Support the eight locked steps and subject palettes.
- [x] Draw supported flowchart arrows after nodes.
- [ ] Add source figure placement with aspect-ratio preservation.
- [ ] Add speaker notes or source mapping.
- [ ] Add formal JSON Schema validation in the build pipeline.

## Phase 3 — Automated quality assurance
- [x] Check minimum slide count, dimensions, optional outline step order, and shape bounds.
- [ ] Check course code, roster, reference slide, and footer branding automatically.
- [ ] Detect text overflow with rendered slide analysis.
- [ ] Automate PNG rendering and contact-sheet generation.
- [ ] Add visual regression samples and accessibility checks.
- [x] Add a sample non-patient demo deck.
- [x] Add a GitHub Actions test/build workflow.

## Phase 4 — Agent integrations
- [ ] Keep `SKILL.md` as the canonical workflow.
- [x] Add GitHub Copilot agent instructions.
- [ ] Test from a clean VS Code checkout with one documented command.
- [ ] Add release/versioning and compatibility notes.

## Release definition of done

- A clean checkout builds a sample deck from non-sensitive demo data.
- All eight steps appear in the correct order.
- Required branding and subject palette are consistently applied.
- The PPTX opens and renders without corruption or obvious clipping.
- Claims and references are traceable to supplied sources.
- Documentation distinguishes implemented features from planned features.

# Proposed architecture

## Design goal

Treat a deck like a reproducible build: source inputs and a structured outline are reviewed first, then rendered into an editable `.pptx`, then checked before delivery.

## Pipeline

1. **Ingest** — extract text and figure references from user-provided DOCX, PDF, PPTX, or notes.
2. **Normalize** — create a case record containing case facts, guide questions, source citations, and unresolved gaps. Do not silently fill gaps.
3. **Plan** — produce a structured outline that maps every slide to one of the eight locked steps.
4. **Review gate** — confirm clinical content and outline before final rendering when requested or when the source is ambiguous.
5. **Render** — use a reusable PowerPoint template and native editable elements where feasible.
6. **Validate** — inspect file integrity, slide bounds, typography, palette, figure aspect ratios, source coverage, and references.
7. **Visual QA** — render slides to images, create a contact sheet, inspect overflow and density, fix, and rerender.
8. **Deliver** — provide PPTX, source outline/data, and a concise QA report; avoid committing case-specific outputs unless explicitly requested.

## Proposed source artifacts

- `case.json`: facts and guide questions extracted from source.
- `outline.json`: approved slide plan with step ID, title, layout type, source IDs, and content blocks.
- `theme.json`: subject palette, typography, margins, and footer settings.
- `build_deck.py`: deterministic PowerPoint renderer.
- `validate_deck.py`: machine-checkable constraints.
- `qa/`: rendered previews and reports for local use; keep patient data out of public commits.

## Outline requirements

Each slide includes `step`, `title`, `layout`, and typed `content`; source IDs should be included when source material is provided. Allowed steps are `cover`, `case`, `questions`, `answers`, `visuals`, `takeaways`, `references`, and `thank-you`. First occurrences must follow that sequence.

## Template inspection

The supplied PowerPoint shell was inspected with python-pptx: 13 slides, 10.0 × 5.625 inches (16:9), one master, and one layout named `DEFAULT`. The layout has no placeholders; slides use positioned shapes and text. The file contains sample content and palette demo pages, so it is a reference deck, not a blank template. The initial renderer therefore creates a new editable deck from the theme rather than overwriting arbitrary sample slides.

## Quality boundaries

Structural validation does not prove text fits, that figures are preserved, that citations are accurate, or that clinical content is correct. These remain separate review gates.

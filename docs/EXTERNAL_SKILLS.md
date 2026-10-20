# External skills and repositories to evaluate

This is a research shortlist, not an endorsement. Before copying code or assets, inspect the current license, dependencies, maintenance status, and implementation. Prefer adapting ideas over copying large blocks of code.

| Project | Useful ideas for G5 | Link |
|---|---|---|
| `anyideaz/pptx-skills` | Template-aware generation; preserving brand fonts, colors, and layouts | https://github.com/anyideaz/pptx-skills |
| `siril9/presentation-skill` | Structured outlines, editable output, reproducible builds, layout validation | https://github.com/siril9/presentation-skill |
| `dev-rathor/dera-presentation-skill` | Outline-first planning, layout variety, iterative visual QA | https://github.com/dev-rathor/dera-presentation-skill |
| `openai/skills` (slides) | PowerPoint generation, rendering and overflow-checking utilities; verify current path and license | https://github.com/openai/skills |
| `ningzimu/awesome-ai-ppt` | Discovery catalog for presentation generators and agent skills | https://github.com/ningzimu/awesome-ai-ppt |

## Evaluation checklist

- Does it preserve existing PowerPoint templates and masters?
- Is output composed of editable PowerPoint elements?
- Can content be represented as structured data and rebuilt deterministically?
- Can it enforce our exact eight-step spine?
- Does it provide rendering, contact sheets, overflow detection, or visual QA?
- Are figures kept at original aspect ratio?
- Can claims be mapped to user-provided sources and Vancouver references?
- Is its license compatible with intended use?
- Can it run in VS Code / GitHub Copilot?

G5 course-specific rules remain authoritative. External skills must not override CSU branding, palettes, source fidelity, or the locked sequence.

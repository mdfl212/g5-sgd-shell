#!/usr/bin/env python3
"""Check the G5 SGD Shell starter package assets; does not validate generated slides."""
from pathlib import Path
import sys, zipfile
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "SKILL.md", ROOT / "CHATGPT_INSTRUCTIONS.md",
    ROOT / "theme.json", ROOT / "schemas" / "outline.schema.json",
    ROOT / "examples" / "demo-outline.json", ROOT / "scripts" / "build_deck.py",
    ROOT / "scripts" / "inspect_template.py", ROOT / "scripts" / "validate_deck.py",
]
OPTIONAL_ASSETS = [
    ROOT / "assets" / "G5_SGD_Shell_Template_MD201-MD207.pptx",
    ROOT / "assets" / "csu_som_shield.png",
]
errors = []
for path in REQUIRED:
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"Missing or empty: {path.relative_to(ROOT)}")
for path in OPTIONAL_ASSETS:
    if path.is_file() and path.suffix.lower() == ".pptx":
        if not zipfile.is_zipfile(path):
            errors.append("Template is not a valid ZIP-based PPTX archive")
        else:
            with zipfile.ZipFile(path) as zf:
                names = set(zf.namelist())
                for member in ("[Content_Types].xml", "ppt/presentation.xml"):
                    if member not in names: errors.append(f"Template is missing required member: {member}")
if errors:
    print("G5 SGD Shell package check: FAIL")
    for error in errors: print(f"- {error}")
    sys.exit(1)
missing = [p.name for p in OPTIONAL_ASSETS if not p.is_file()]
print("G5 SGD Shell package check: PASS" if not missing else "G5 SGD Shell source check: PASS (binary assets not yet uploaded)")
if missing: print("Missing optional binary assets: " + ", ".join(missing))
print("This check does not validate clinical claims, citations, or visual rendering.")

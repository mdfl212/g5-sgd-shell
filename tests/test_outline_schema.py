"""Lightweight tests for locked G5 outline rules; uses only the standard library."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_STEPS = ["cover", "case", "questions", "answers", "visuals", "takeaways", "references", "thank-you"]

class ThemeTests(unittest.TestCase):
    def test_subject_palette_has_all_modules(self):
        theme = json.loads((ROOT / "theme.json").read_text(encoding="utf-8"))
        self.assertEqual(set(theme["subjects"]), {f"MD{n}" for n in range(201, 208)})
        for palette in theme["subjects"].values():
            for key in ("banner", "subhead", "accent", "softBg"):
                self.assertRegex(palette[key], r"^#[0-9A-Fa-f]{6}$")

    def test_locked_steps_are_ordered_and_unique(self):
        theme = json.loads((ROOT / "theme.json").read_text(encoding="utf-8"))
        steps = [item["id"] for item in theme["lockedSteps"]]
        self.assertEqual(steps, EXPECTED_STEPS)
        self.assertEqual(len(steps), len(set(steps)))

    def test_outline_schema_declares_locked_steps(self):
        schema = json.loads((ROOT / "schemas" / "outline.schema.json").read_text(encoding="utf-8"))
        step_enum = schema["properties"]["slides"]["items"]["properties"]["step"]["enum"]
        self.assertEqual(step_enum, EXPECTED_STEPS)

if __name__ == "__main__":
    unittest.main()

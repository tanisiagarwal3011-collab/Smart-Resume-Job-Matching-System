import os
import sys
import unittest

# Add the project root to Python's import path
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

from parser import extract_pdf_text


class TestParser(unittest.TestCase):

    def test_pdf_extraction(self):
        resume_path = os.path.join(
            PROJECT_ROOT,
            "resume.pdf"
        )

        text = extract_pdf_text(resume_path)

        self.assertIsInstance(text, str)
        self.assertGreater(len(text.strip()), 0)


if __name__ == "__main__":
    unittest.main()

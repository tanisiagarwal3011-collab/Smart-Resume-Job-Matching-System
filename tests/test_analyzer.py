import os
import sys
import unittest
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)
from analyzer import (
    detect_resume_sections,
    analyze_education_requirement,
    analyze_experience_requirement
)
class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.resume_text = """
        Computer Science Engineering Student
        Skills:
        Python, Java, SQL
        Education:
        Bachelor of Technology in Computer Science Engineering
        Experience:
        Software Developer Intern with experience in Python and Flask.
        Projects:
        Developed web applications using Python and Flask.
        """
        self.job_text = """
        Software Developer
        Requirements:
        Bachelor degree in Computer Science.
        Experience with Python development and web applications.
        """
    def test_resume_sections(self):
        sections = detect_resume_sections(
            self.resume_text
        )
        self.assertTrue(sections["Skills"])
        self.assertTrue(sections["Education"])
        self.assertTrue(sections["Experience"])
        self.assertTrue(sections["Projects"])
    def test_education_analysis(self):
        matched, required, percentage = (
            analyze_education_requirement(
                self.resume_text,
                self.job_text
            )
        )
        self.assertGreater(len(required), 0)
        self.assertGreater(len(matched), 0)
        self.assertGreater(percentage, 0)
    def test_experience_analysis(self):
        matched, required, percentage = (
            analyze_experience_requirement(
                self.resume_text,
                self.job_text
            )
        )
        self.assertGreater(len(required), 0)
        self.assertGreater(len(matched), 0)
        self.assertGreater(percentage, 0)
if __name__ == "__main__":
    unittest.main()

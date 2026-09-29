import os
import sys
import unittest
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)
from matcher import (
    calculate_skill_match,
    calculate_text_similarity
)
class TestMatcher(unittest.TestCase):
    def test_skill_match(self):
        resume_skills = [
            "Python",
            "SQL",
            "Flask",
            "Git"
        ]
        job_skills = [
            "Python",
            "SQL",
            "Flask",
            "Git",
            "Docker",
            "AWS"
        ]
        matched, missing, percentage = calculate_skill_match(
            job_skills,
            resume_skills
        )
        self.assertEqual(
            matched,
            ["Python", "SQL", "Flask", "Git"]
        )
        self.assertEqual(
            missing,
            ["Docker", "AWS"]
        )
        self.assertAlmostEqual(
            percentage,
            66.6667,
            places=2
        )
    def test_empty_job_skills(self):
        matched, missing, percentage = calculate_skill_match(
            [],
            ["Python"]
        )
        self.assertEqual(matched, [])
        self.assertEqual(missing, [])
        self.assertEqual(percentage, 0)
    def test_text_similarity(self):
        resume_text = """
        Python Flask SQL software development
        """
        job_text = """
        Python Flask SQL software development
        """
        similarity = calculate_text_similarity(
            resume_text,
            job_text
        )
        self.assertAlmostEqual(
            similarity,
            100.0,
            places=2
        )
if __name__ == "__main__":
    unittest.main()

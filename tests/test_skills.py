import os
import sys
import unittest
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, PROJECT_ROOT)
from skills import load_skills, find_skills
class TestSkills(unittest.TestCase):
    def test_load_skills(self):
        skills_file = os.path.join(
            PROJECT_ROOT,
            "skills.txt"
        )
        skills = load_skills(skills_file)
        self.assertIsInstance(skills, list)
        self.assertGreater(len(skills), 0)
    def test_find_skills(self):
        skills = [
            "Python",
            "Java",
            "C++",
            "SQL",
            "Flask"
        ]
        text = "I have experience with Python, C++, SQL and Flask."
        found_skills = find_skills(
            text,
            skills
        )
        self.assertIn("Python", found_skills)
        self.assertIn("C++", found_skills)
        self.assertIn("SQL", found_skills)
        self.assertIn("Flask", found_skills)
    def test_skill_not_found(self):
        skills = [
            "Python",
            "Java",
            "SQL"
        ]
        text = "I have experience with Python."
        found_skills = find_skills(
            text,
            skills
        )
        self.assertNotIn("Java", found_skills)
        self.assertNotIn("SQL", found_skills)
if __name__ == "__main__":
    unittest.main()

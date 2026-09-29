import re
def load_skills(file_path):
    """
    Load skills from the skills database.
    """
    with open(file_path, "r") as file:
        skills = file.read().splitlines()
    return [skill.strip() for skill in skills if skill.strip()]
def find_skills(text, skills):
    """
    Find skills accurately in the given text.
    """
    found_skills = []
    text_lower = text.lower()
    for skill in skills:
        skill_pattern = (
            r"(?<!\w)"
            + re.escape(skill.lower())
            + r"(?!\w)"
        )
        if re.search(skill_pattern, text_lower):
            found_skills.append(skill)
    return found_skills



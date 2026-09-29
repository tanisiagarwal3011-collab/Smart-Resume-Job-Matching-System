def detect_resume_sections(resume_text):
    """
    Detect important sections present in the resume.
    """
    sections = {
        "Skills": False,
        "Education": False,
        "Experience": False,
        "Projects": False
    }
    lines = resume_text.splitlines()
    for line in lines:
        line = line.strip().lower()
        if line == "skills:" or line == "skills":
            sections["Skills"] = True
        elif line == "education:" or line == "education":
            sections["Education"] = True
        elif line == "experience:" or line == "experience":
            sections["Experience"] = True
        elif line == "projects:" or line == "projects":
            sections["Projects"] = True
    return sections
def analyze_education_requirement(resume_text, job_text):
    """
    Analyze whether the resume contains education-related
    information required by the job description.
    """
    education_keywords = [
        "bachelor",
        "b.tech",
        "b.e.",
        "degree",
        "computer science",
        "computer engineering"
    ]
    job_lower = job_text.lower()
    resume_lower = resume_text.lower()
    required_keywords = []
    matched_keywords = []
    for keyword in education_keywords:
        if keyword in job_lower:
            required_keywords.append(keyword)
            if keyword in resume_lower:
                matched_keywords.append(keyword)
    if len(required_keywords) > 0:
        percentage = (
            len(matched_keywords) /
            len(required_keywords)
        ) * 100
    else:
        percentage = 100
    return matched_keywords, required_keywords, percentage
def analyze_experience_requirement(resume_text, job_text):
    """
    Analyze experience-related requirements in the job description.
    """
    experience_keywords = [
        "experience",
        "python development",
        "software development",
        "web development",
        "web applications",
        "software developer",
        "developer"
    ]
    job_lower = job_text.lower()
    resume_lower = resume_text.lower()
    required_keywords = []
    matched_keywords = []
    for keyword in experience_keywords:
        if keyword in job_lower:
            required_keywords.append(keyword)
            if keyword in resume_lower:
                matched_keywords.append(keyword)
    if len(required_keywords) > 0:
        percentage = (
            len(matched_keywords) /
            len(required_keywords)
        ) * 100
    else:
        percentage = 100
    return matched_keywords, required_keywords, percentage
if __name__ == "__main__":
    resume_text = """
    Computer Science Engineering Student
    Education:
    Bachelor of Technology in Computer Science Engineering
    Experience:
    Software Developer Intern with experience in Python and Flask.
    Projects:
    Developed web applications using Python and Flask.
    """
    job_text = """
    Software Developer
    Requirements:
    Bachelor degree in Computer Science.
    Experience with Python development and web applications.
    """
    sections = detect_resume_sections(resume_text)
    print("Resume Sections:")
    print(sections)
    matched_education, required_education, education_score = (
        analyze_education_requirement(
            resume_text,
            job_text
        )
    )
    print("\nEducation:")
    print("Matched:", matched_education)
    print("Required:", required_education)
    print("Match:", round(education_score, 2), "%")
    matched_experience, required_experience, experience_score = (
        analyze_experience_requirement(
            resume_text,
            job_text
        )
    )
    print("\nExperience:")
    print("Matched:", matched_experience)
    print("Required:", required_experience)
    print("Match:", round(experience_score, 2), "%")

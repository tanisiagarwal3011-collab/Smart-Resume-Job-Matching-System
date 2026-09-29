from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def calculate_skill_match(job_skills, resume_skills):
    """
    Compare job-required skills with skills found in the resume.
    """
    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]
    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]
    if len(job_skills) > 0:
        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100
    else:
        match_percentage = 0

    return matched_skills, missing_skills, match_percentage
def calculate_text_similarity(resume_text, job_text):
    """
    Calculate similarity between resume and job description
    using TF-IDF and cosine similarity.
    """
    documents = [resume_text, job_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0] * 100
    return similarity
if __name__ == "__main__":
    resume_skills = ["Python", "SQL", "Flask", "Git"]
    job_skills = [
        "Python",
        "SQL",
        "Flask",
        "Git",
        "Docker",
        "Kubernetes",
        "AWS"
    ]
    matched, missing, score = calculate_skill_match(
        job_skills,
        resume_skills
    )
    print("Matched Skills:", matched)
    print("Missing Skills:", missing)
    print("Skill Match:", round(score, 2), "%")
    resume_text = """
    Python Flask SQL Git software development
    """
    job_text = """
    Python Flask SQL Git Docker Kubernetes AWS
    """
    similarity = calculate_text_similarity(
        resume_text,
        job_text
    )
    print("Text Similarity:", round(similarity, 2), "%")

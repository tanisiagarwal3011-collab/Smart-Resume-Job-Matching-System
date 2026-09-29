import os
from parser import extract_pdf_text
from skills import load_skills, find_skills
from matcher import calculate_skill_match, calculate_text_similarity
from analyzer import (
    detect_resume_sections,
    analyze_education_requirement,
    analyze_experience_requirement)
from reporter import generate_report, display_report
from utils import validate_file, read_text_file, validate_text
print("========================================")
print("     SMART RESUME & JOB MATCHER")
print("========================================")
print()
try:
    # ----------------------------------------
    # Project File Paths
    # ----------------------------------------
    project_folder = os.path.dirname(os.path.abspath(__file__))
    resume_file = os.path.join(project_folder, "samples", "resume.pdf")
    job_file = os.path.join(project_folder, "samples", "job.txt")
    skills_file = os.path.join(project_folder,"data", "skills.txt")
    # ----------------------------------------
    # Load Resume
    # ----------------------------------------
    validate_file(resume_file)
    resume_text = extract_pdf_text(resume_file)
    validate_text(resume_text, "Resume")
    # ----------------------------------------
    # Load Job Description
    # ----------------------------------------
    validate_file(job_file)
    job_text = read_text_file(job_file)
    validate_text(job_text, "Job Description")
    # ----------------------------------------
    # Load Skills Database
    # ----------------------------------------
    validate_file(skills_file)
    skills = load_skills(skills_file)
    print("Resume PDF loaded successfully!")
    print("Job description loaded successfully!")
    print("Skills database loaded successfully!")
    # ----------------------------------------
    # Find Skills
    # ----------------------------------------
    resume_skills = find_skills(
        resume_text,
        skills
    )
    job_skills = find_skills(
        job_text,
        skills
    )
    # ----------------------------------------
    # Skill Matching
    # ----------------------------------------
    matched_skills, missing_skills, match_percentage = (
        calculate_skill_match(
            job_skills,
            resume_skills
        )
    )
    # ----------------------------------------
    # Text Similarity
    # ----------------------------------------
    text_similarity = calculate_text_similarity(
        resume_text,
        job_text
    )
    # ----------------------------------------
    # Resume Section Analysis
    # ----------------------------------------
    sections = detect_resume_sections(
        resume_text
    )
    # ----------------------------------------
    # Education Requirement
    # ----------------------------------------
    (
        education_matches,
        education_requirements,
        education_percentage
    ) = analyze_education_requirement(
        resume_text,
        job_text
    )
    # ----------------------------------------
    # Experience Requirement
    # ----------------------------------------
    (
        experience_matches,
        experience_requirements,
        experience_percentage
    ) = analyze_experience_requirement(
        resume_text,
        job_text
    )
    # ----------------------------------------
    # Calculate Overall Match Score
    # ----------------------------------------
    overall_score = (
        (match_percentage * 0.50)
        + (text_similarity * 0.30)
        + (experience_percentage * 0.20)
    )
    # ----------------------------------------
    # Resume Skills
    # ----------------------------------------
    print()
    print("----------- RESUME SKILLS -----------")
    for skill in resume_skills:
        print("✓", skill)
    # ----------------------------------------
    # Job Required Skills
    # ----------------------------------------
    print()
    print("-------- JOB REQUIRED SKILLS --------")
    for skill in job_skills:
        print("•", skill)
    # ----------------------------------------
    # Matched Skills
    # ----------------------------------------
    print()
    print("----------- MATCHED SKILLS -----------")
    for skill in matched_skills:
        print("✓", skill)
    # ----------------------------------------
    # Missing Skills
    # ----------------------------------------
    print()
    print("----------- MISSING SKILLS -----------")
    for skill in missing_skills:
        print("✗", skill)
    # ----------------------------------------
    # Matching Result
    # ----------------------------------------
    print()
    print("========================================")
    print("          MATCHING RESULT")
    print("========================================")
    print("Required Skills :", len(job_skills))
    print("Matched Skills  :", len(matched_skills))
    print("Missing Skills  :", len(missing_skills))
    print()
    print(
        "Skill Match:",
        round(match_percentage, 2),
        "%"
    )
    print(
        "Text Similarity:",
        round(text_similarity, 2),
        "%"
    )
    # ----------------------------------------
    # Resume Section Analysis
    # ----------------------------------------
    print()
    print("========================================")
    print("       RESUME SECTION ANALYSIS")
    print("========================================")
    for section, found in sections.items():
        if found:
            print("✓", section, ": Detected")
        else:
            print("✗", section, ": Not Detected")
    print("========================================")
    # ----------------------------------------
    # Job Requirement Analysis
    # ----------------------------------------
    print()
    print("========================================")
    print("       JOB REQUIREMENT ANALYSIS")
    print("========================================")
    # Education
    print()
    print("Education Requirement:")
    if education_matches:
        print(
            "✓ Education requirement appears to be matched"
        )
    else:
        print(
            "✗ Education requirement not detected in resume"
        )
    print()
    print("Required Education Keywords:")
    for keyword in education_requirements:
        print("•", keyword)
    print("========================================")
    # Experience
    print()
    print("Experience Requirement:")
    print("----------------------------------------")
    if experience_matches:
        print("✓ Relevant experience detected")
        print()
        print("Matched Experience Keywords:")
        for keyword in experience_matches:
            print("✓", keyword)
    else:
        print("✗ Relevant experience not detected")
    print()
    print(
        "Experience Keyword Match:",
        round(experience_percentage, 2),
        "%"
    )
    print("========================================")
    # ----------------------------------------
    # Final Match Analysis
    # ----------------------------------------
    print()
    print("========================================")
    print("          FINAL MATCH ANALYSIS")
    print("========================================")
    print(
        "Skill Match       :",
        round(match_percentage, 2),
        "%"
    )
    print(
        "Text Similarity   :",
        round(text_similarity, 2),
        "%"
    )
    print(
        "Experience Match  :",
        round(experience_percentage, 2),
        "%"
    )
    print()
    print(
        "Overall Match     :",
        round(overall_score, 2),
        "%"
    )
    print("========================================")
    # ----------------------------------------
    # Generate Final Report
    # ----------------------------------------
    report = generate_report(
        matched_skills,
        missing_skills,
        match_percentage,
        text_similarity,
        experience_percentage,
        overall_score
    )
    display_report(report)
# ----------------------------------------
# Error Handling
# ----------------------------------------
except FileNotFoundError as error:
    print()
    print("ERROR:", error)
except ValueError as error:
    print()
    print("ERROR:", error)
except Exception as error:
    print()
    print("UNEXPECTED ERROR:", error)
def generate_recommendations(missing_skills):
    """
    Generate recommendations based on missing skills.
    """
    recommendations = []
    for skill in missing_skills:
        recommendations.append(
            f"Improve knowledge of {skill}"
        )
    return recommendations
def generate_report(
    matched_skills,
    missing_skills,
    skill_match_percentage,
    text_similarity,
    experience_percentage,
    overall_match
):
    """
    Generate the final resume-job matching report.
    """
    recommendations = generate_recommendations(missing_skills)
    report = {
        "strengths": matched_skills,
        "missing_skills": missing_skills,
        "recommendations": recommendations,
        "skill_match": skill_match_percentage,
        "text_similarity": text_similarity,
        "experience_match": experience_percentage,
        "overall_match": overall_match
    }
    return report
def display_report(report):
    """
    Display the final analysis report in the terminal.
    """
    print()
    print("========================================")
    print("           MATCHING RESULTS")
    print("========================================")
    print()
    print(
        f"Skill Match: "
        f"{report['skill_match']:.2f}%"
    )
    print(
        f"Text Similarity: "
        f"{report['text_similarity']:.2f}%"
    )
    print(
        f"Experience Match: "
        f"{report['experience_match']:.1f}%"
    )
    print(
        f"Overall Match: "
        f"{report['overall_match']:.2f}%"
    )
    print()
    print("Strengths:")
    if report["strengths"]:
        for skill in report["strengths"]:
            print(f"✓ {skill}")
    else:
        print("None identified")
    print()
    print("Missing Skills:")
    if report["missing_skills"]:
        for skill in report["missing_skills"]:
            print(f"✗ {skill}")
    else:
        print("None")
    print()
    print("Recommendations:")
    if report["recommendations"]:
        for recommendation in report["recommendations"]:
            print(f"→ {recommendation}")
    else:
        print("No recommendations")
    print()
    print("========================================")
    print("          ANALYSIS COMPLETE")
    print("========================================")
if __name__ == "__main__":
    matched_skills = [
        "Python",
        "SQL",
        "Flask",
        "Git"
    ]
    missing_skills = [
        "Docker",
        "Kubernetes",
        "AWS"
    ]
    report = generate_report(
        matched_skills,
        missing_skills,
        57.14,
        55.12,
        80.0,
        61.11
    )
    display_report(report)

def generate_recommendations(score, missing_skills):

    recommendations = []

    if score < 50:
        recommendations.append(
            "Your resume has low ATS match. Add more job-related keywords."
        )

    if "aws" in missing_skills:
        recommendations.append(
            "Consider learning AWS or adding cloud projects."
        )

    if "docker" in missing_skills:
        recommendations.append(
            "Add Docker skills for better backend/devops compatibility."
        )

    if len(missing_skills) > 5:
        recommendations.append(
            "Your resume lacks several required technical skills."
        )

    return recommendations
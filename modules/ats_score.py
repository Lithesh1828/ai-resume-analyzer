from modules.skill_extractor import extract_skills

def calculate_ats_score(resume_text, job_description):

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    matched_skills = list(
        set(resume_skills) & set(job_skills)
    )

    if len(job_skills) == 0:
        return 0, [], []

    score = (
        len(matched_skills) / len(job_skills)
    ) * 100

    missing_skills = list(
        set(job_skills) - set(resume_skills)
    )

    return round(score, 2), matched_skills, missing_skills
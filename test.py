from modules.ats_score import calculate_ats_score

resume_text = """
Python SQL Machine Learning Pandas
"""

job_description = """
Python SQL AWS Docker Machine Learning
"""

score, matched, missing = calculate_ats_score(
    resume_text,
    job_description
)

print("ATS Score:", score)

print("Matched Skills:", matched)

print("Missing Skills:", missing)
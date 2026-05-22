def classify_resume(text):

    text = text.lower()

    if "machine learning" in text or "deep learning" in text:
        return "Data Science"

    elif "react" in text or "javascript" in text:
        return "Frontend Developer"

    elif "django" in text or "flask" in text:
        return "Backend Developer"

    elif "aws" in text or "docker" in text:
        return "Cloud / DevOps"

    else:
        return "General Software Role"
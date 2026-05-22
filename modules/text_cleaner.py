import re
import string

def clean_text(text):

    text = text.lower()

    text = re.sub(r'\n', ' ', text)

    text = re.sub(r'\s+', ' ', text)

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    return text
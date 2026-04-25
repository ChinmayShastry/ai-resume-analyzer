import re
from config import COMMON_SKILLS


def normalize_text(text: str) -> str:
    # Lowercase + remove special chars
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return text


def extract_skills(text: str):
    text = normalize_text(text)

    found_skills = []

    for skill in COMMON_SKILLS:
        # Create strict word boundary match
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'

        if re.search(pattern, text):
            found_skills.append(skill.lower())

    return list(set(found_skills))

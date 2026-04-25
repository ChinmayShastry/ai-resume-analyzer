from config import COMMON_SKILLS


def extract_skills(text: str):

    text_lower = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))
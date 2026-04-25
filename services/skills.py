import re

def normalize(text):
    return re.sub(r'[^a-z0-9 ]', ' ', text.lower())

def extract_skills(text):
    text = normalize(text)
    found = []

    for skill in COMMON_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found.append(skill)

    return list(set(found))

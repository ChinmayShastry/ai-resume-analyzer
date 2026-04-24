import re

def extract_skills(text: str):

    common_skills = [
        "python", "java", "c++", "sql", "machine learning",
        "deep learning", "nlp", "tensorflow", "pytorch",
        "react", "node", "fastapi", "streamlit"
    ]

    text_lower = text.lower()

    found_skills = []

    for skill in common_skills:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))

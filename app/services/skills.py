import re

# Small but strong baseline skill list (expand later)
SKILL_DB = [
    "python", "java", "c++", "sql", "machine learning", "deep learning",
    "nlp", "computer vision", "pytorch", "tensorflow", "scikit-learn",
    "fastapi", "flask", "docker", "kubernetes", "aws", "gcp",
    "data structures", "algorithms", "llm", "transformers"
]

def extract_skills(text: str):
    text = text.lower()
    
    found_skills = set()

    for skill in SKILL_DB:
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)


from dotenv import load_dotenv
load_dotenv()


from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_skills_llm(text: str):
    prompt = f"""
    Extract technical skills from the text below.
    Return ONLY a JSON list of skills.

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        skills = json.loads(response.choices[0].message.content)
        return skills
    except:
        return []
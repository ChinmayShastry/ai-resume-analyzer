from dotenv import load_dotenv
load_dotenv()


import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_feedback(resume, jd):
    prompt = f"""
    Analyze the resume against the job description.

    Resume:
    {resume}

    Job Description:
    {jd}

    Provide:
    - Strengths
    - Weaknesses
    - Missing skills
    - Suggestions
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
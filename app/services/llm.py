from openai import OpenAI
from app.config import MODEL_NAME, RESUME_FEEDBACK_PROMPT


def get_client(api_key: str):
    return OpenAI(api_key=api_key)


def get_feedback(resume: str, jd: str, api_key: str):

    if not api_key:
        raise ValueError("OpenAI API key is missing")

    client = get_client(api_key)

    prompt = f"""
{RESUME_FEEDBACK_PROMPT}

Resume:
{resume}

Job Description:
{jd}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

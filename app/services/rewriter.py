from openai import OpenAI
from app.config import MODEL_NAME, RESUME_REWRITE_PROMPT


def get_client(api_key: str):
    return OpenAI(api_key=api_key)


def rewrite_bullet_points(resume_text: str, api_key: str):

    client = get_client(api_key)

    prompt = f"""
{RESUME_REWRITE_PROMPT}

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

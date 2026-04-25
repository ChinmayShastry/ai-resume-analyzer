from openai import OpenAI
from config import MODEL_NAME, TEMPERATURE, RESUME_FEEDBACK_PROMPT


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
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE
    )

    return response.choices[0].message.content


def get_full_analysis(resume: str, jd: str, api_key: str):

    if not api_key:
        raise ValueError("OpenAI API key is missing")

    client = get_client(api_key)

    from config import RESUME_MASTER_PROMPT

    prompt = f"""
{RESUME_MASTER_PROMPT}

Resume:
{resume}

Job Description:
{jd}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE
    )

    content = response.choices[0].message.content

    # --- Split response ---
    feedback = ""
    rewrite = ""

    if "===REWRITE===" in content:
        parts = content.split("===REWRITE===")
        feedback = parts[0].replace("===FEEDBACK===", "").strip()
        rewrite = parts[1].strip()
    else:
        feedback = content  # fallback

    return feedback, rewrite

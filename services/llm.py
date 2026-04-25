from openai import OpenAI
from config import MODEL_NAME, TEMPERATURE, RESUME_MASTER_PROMPT


def get_client(api_key: str):
    return OpenAI(api_key=api_key)


def get_full_analysis(resume: str, jd: str, api_key: str):
    """
    Returns:
        feedback (str)
        rewritten_resume (str)
    """

    # -------- VALIDATION --------
    if not api_key:
        raise ValueError("OpenAI API key is missing")

    client = get_client(api_key)

    # -------- PROMPT --------
    prompt = f"""
{RESUME_MASTER_PROMPT}

Resume:
{resume}

Job Description:
{jd}
"""

    # -------- API CALL --------
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=TEMPERATURE
        )

        content = response.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {str(e)}", "Rewrite unavailable"

    # -------- PARSE RESPONSE --------
    feedback = ""
    rewrite = ""

    try:
        if "===REWRITE===" in content:
            parts = content.split("===REWRITE===")

            feedback = parts[0].replace("===FEEDBACK===", "").strip()
            rewrite = parts[1].strip()
        else:
            # fallback if model doesn't follow format
            feedback = content
            rewrite = "Rewrite not properly generated"

    except Exception:
        feedback = content
        rewrite = "Error parsing rewrite"

    return feedback, rewrite

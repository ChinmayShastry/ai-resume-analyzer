from openai import OpenAI

def get_client(api_key):
    return OpenAI(api_key=api_key)


def rewrite_bullet_points(resume_text: str, api_key: str):

    client = get_client(api_key)

    prompt = f"""
Improve resume bullet points:

- Make action oriented
- Add impact
- ATS friendly
- No fake info

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

from openai import OpenAI

def get_client(api_key):
    return OpenAI(api_key=api_key)


def get_feedback(resume, jd, api_key):

    client = get_client(api_key)

    prompt = f"""
Analyze resume vs job description.

Resume:
{resume}

Job:
{jd}

Give:
- strengths
- weaknesses
- missing skills
- suggestions
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

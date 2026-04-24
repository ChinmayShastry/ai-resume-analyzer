from dotenv import load_dotenv
load_dotenv()



from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_bullet_points(resume_text: str):
    prompt = f"""
You are an expert resume writer.

Improve the following resume bullet points:
- Make them strong, action-oriented
- Add measurable impact where possible
- Keep them ATS-friendly
- Do NOT add fake experience

Return in bullet format.

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
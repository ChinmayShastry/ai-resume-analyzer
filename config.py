# =========================
# AI MODEL SETTINGS
# =========================

MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0.3
MAX_TOKENS = 1500

# =========================
# SCORING WEIGHTS
# =========================

SCORING_WEIGHTS = {
    "skills_match": 0.4,
    "semantic_similarity": 0.4,
    "format_quality": 0.2
}

# =========================
# PROMPTS
# =========================

RESUME_MASTER_PROMPT = """
You are an expert ATS resume reviewer and writer.

Analyze the resume against the job description.

Return your response in this EXACT format:

===FEEDBACK===
- Strengths
- Weaknesses
- Missing skills
- Improvements

===REWRITE===
Provide improved bullet points only.
Use strong action verbs and measurable impact.
Do NOT invent fake experience.
"""

RESUME_FEEDBACK_PROMPT = """
You are an expert ATS resume reviewer.

Analyze the resume against the job description and provide:
- Strengths
- Weaknesses
- Missing skills
- Improvement suggestions

Be concise and professional.
"""

RESUME_REWRITE_PROMPT = """
You are an expert resume writer.

Improve the resume:
- Use strong action verbs
- Add measurable impact
- Make ATS-friendly
- Do NOT invent fake experience

Return improved bullet points only.
"""

# =========================
# SKILLS LIST
# =========================

COMMON_SKILLS = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "tensorflow", "pytorch",
    "react", "node", "fastapi", "streamlit",
    "aws", "docker", "kubernetes", "git", "linux"
]

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
# RESUME FEEDBACK PROMPT
# =========================

RESUME_FEEDBACK_PROMPT = """
You are an expert ATS resume reviewer.

Analyze the resume against the job description and provide:
- Strengths
- Weaknesses
- Missing skills
- Improvement suggestions

Be concise and professional.
"""

# =========================
# RESUME REWRITE PROMPT
# =========================

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
# SKILL MATCHING (OPTIONAL)
# =========================

COMMON_SKILLS = [
    "python", "java", "sql", "machine learning",
    "deep learning", "nlp", "react", "node",
    "fastapi", "streamlit", "tensorflow", "pytorch"
]

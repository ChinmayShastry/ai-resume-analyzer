from fastapi import APIRouter, UploadFile, File, Form

from app.services.parser import extract_text_from_pdf
from app.services.skills import extract_skills
from app.services.gap_analysis import compute_gap
from app.services.embeddings import compute_similarity
from app.services.scorer import calculate_score
from app.services.llm import get_feedback

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_text = extract_text_from_pdf(file)

    # 🧠 Skill extraction
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    # 📊 Gap analysis
    gap_result = compute_gap(resume_skills, jd_skills)

    # 🤖 Semantic similarity
    similarity = compute_similarity(resume_text, job_description)
    score = calculate_score(similarity)

    # 💬 LLM feedback
    feedback = get_feedback(resume_text, job_description)

    return {
        "score": score,
        "semantic_similarity": similarity,
        "skills": {
            "resume_skills": resume_skills,
            "jd_skills": jd_skills,
            "analysis": gap_result
        },
        "feedback": feedback
    }


from app.services.rewriter import rewrite_bullet_points

@router.post("/rewrite")
async def rewrite_resume(file: UploadFile = File(...)):
    resume_text = extract_text_from_pdf(file)
    
    improved_resume = rewrite_bullet_points(resume_text)

    return {
        "rewritten_resume": improved_resume
    }
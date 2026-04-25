import streamlit as st
import plotly.express as px

from services.parser import extract_text_from_pdf
from services.skills import extract_skills
from services.gap_analysis import compute_gap
from services.embeddings import compute_similarity
from services.scorer import calculate_score
from services.llm import get_full_analysis
from services.pdf_exporter import generate_resume_pdf
from utils.text_splitter import split_resume_sections

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ---------------- SESSION ----------------
if "result" not in st.session_state:
    st.session_state.result = None

# ---------------- HEADER ----------------
st.title("🚀 AI Resume Analyzer")

st.markdown("""
Improve your resume with AI

- 📊 Match score
- 🧠 Skill gap analysis
- 💬 AI feedback
- ✍️ Resume rewriting
- 📂 Section-wise breakdown
""")

st.write("---")

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

with col2:
    jd = st.text_area("🧾 Paste Job Description", height=150)

api_key = st.text_input("🔑 OpenAI API Key", type="password")

colA, colB = st.columns(2)

with colA:
    analyze = st.button("🚀 Analyze Resume", use_container_width=True)

with colB:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.result = None
        st.rerun()

# ---------------- ANALYSIS ----------------
if analyze and file and jd:

    if not api_key:
        st.error("Please enter API key")
        st.stop()

    with st.spinner("🧠 AI is analyzing your resume..."):

        resume_text = extract_text_from_pdf(file)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd)

        gap = compute_gap(resume_skills, jd_skills)

        similarity = compute_similarity(resume_text, jd)
        score = calculate_score(similarity, gap)

        feedback, rewritten = get_full_analysis(resume_text, jd, api_key)    

        # ✅ NEW: section splitting (FIXED POSITION)
        sections = split_resume_sections(resume_text)

        st.session_state.result = {
            "resume_text": resume_text,
            "gap": gap,
            "score": score,
            "feedback": feedback,
            "rewritten": rewritten,
            "sections": sections
        }

# ---------------- OUTPUT ----------------
data = st.session_state.result

if data:

    st.markdown("## 📊 Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Score", f"{data['score']}%")
    col2.metric("Matched Skills", len(data["gap"]["matched_skills"]))
    col3.metric("Missing Skills", len(data["gap"]["missing_skills"]))

    st.markdown("## 🧠 Skill Analysis")

    c1, c2 = st.columns(2)

    with c1:
        st.success("Matched Skills")
        st.write(data["gap"]["matched_skills"])

    with c2:
        st.error("Missing Skills")
        st.write(data["gap"]["missing_skills"])

    # ---------------- NEW FEATURE ----------------
    st.markdown("## 📂 Resume Sections")
    for section, content in data["sections"].items():
        st.subheader(section.capitalize())
        st.text(content.strip())

    st.markdown("## 💬 AI Feedback")
    st.info(data["feedback"])

    st.markdown("## ✍️ Improved Resume")
    st.code(data["rewritten"])

    st.markdown("## 📥 Download")

    pdf_buffer = generate_resume_pdf(
        data["resume_text"],
        data["rewritten"],
        data["score"]
    )

    st.download_button(
        "⬇️ Download PDF",
        pdf_buffer,
        "ai_resume.pdf",
        "application/pdf"
    )

else:
    st.info("Upload resume and job description to start analysis")

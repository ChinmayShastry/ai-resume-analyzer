import streamlit as st
import plotly.express as px

from services.parser import extract_text_from_pdf
from services.skills import extract_skills
from services.gap_analysis import compute_gap
from services.embeddings import compute_similarity
from services.scorer import calculate_score
from services.llm import get_feedback
from services.rewriter import rewrite_bullet_points
from services.pdf_exporter import generate_resume_pdf

# ---------------- UI CONFIG ----------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "result" not in st.session_state:
    st.session_state.result = None

# ---------------- HEADER ----------------
st.markdown("""
    <h1 style='text-align: center; color: #4F46E5;'>
        🚀 AI Resume Analyzer
    </h1>
    <p style='text-align: center; color: gray;'>
        AI-powered resume scoring, skill gap detection & optimization
    </p>
""", unsafe_allow_html=True)

st.write("---")

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 2])

# ================= LEFT PANEL =================
with col1:
    st.subheader("📤 Upload Section")

    file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    jd = st.text_area("Paste Job Description")

    analyze = st.button("🚀 Analyze Resume")

    # RESET OPTION (GOOD UX)
    if st.button("🔄 Reset"):
        st.session_state.result = None
        st.rerun()

# ================= ANALYSIS PIPELINE =================
if analyze and file and jd:

    with st.spinner("🧠 AI is analyzing your resume..."):

        resume_text = extract_text_from_pdf(file)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd)

        gap = compute_gap(resume_skills, jd_skills)

        similarity = compute_similarity(resume_text, jd)
        score = calculate_score(similarity)

        feedback = get_feedback(resume_text, jd)
        rewritten = rewrite_bullet_points(resume_text)

        # SAVE RESULT ONCE (IMPORTANT FIX)
        st.session_state.result = {
            "resume_text": resume_text,
            "resume_skills": resume_skills,
            "jd_skills": jd_skills,
            "gap": gap,
            "score": score,
            "feedback": feedback,
            "rewritten": rewritten
        }

# ================= RIGHT PANEL =================
with col2:

    data = st.session_state.result

    if data:

        st.markdown("### 📊 Resume Score")
        st.metric(label="Match Score", value=f"{data['score']}%")

        st.markdown("### 📈 Skill Match Overview")

        fig = px.bar(
            x=["Matched Skills", "Missing Skills"],
            y=[len(data["gap"]["matched_skills"]), len(data["gap"]["missing_skills"])],
            color=["Matched", "Missing"],
            color_discrete_map={
                "Matched": "#22c55e",
                "Missing": "#ef4444"
            }
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 🧠 Skill Analysis")

        c1, c2 = st.columns(2)

        with c1:
            st.success("✅ Matched Skills")
            st.write(data["gap"]["matched_skills"])

        with c2:
            st.error("❌ Missing Skills")
            st.write(data["gap"]["missing_skills"])

        st.markdown("### 💬 AI Feedback")
        st.info(data["feedback"])

        st.markdown("### ✍️ AI Improved Resume")
        st.code(data["rewritten"], language="markdown")

        # ---------------- PDF DOWNLOAD ----------------
        st.markdown("### 📥 Download Report")

        pdf_buffer = generate_resume_pdf(
            data["resume_text"],
            data["rewritten"],
            data["score"]
        )

        st.download_button(
            label="⬇️ Download Optimized Resume PDF",
            data=pdf_buffer,
            file_name="ai_optimized_resume.pdf",
            mime="application/pdf"
        )

    else:
        st.markdown("""
        <div style='text-align:center; padding: 40px; color: gray;'>
            Upload your resume and job description to get AI analysis
        </div>
        """, unsafe_allow_html=True)
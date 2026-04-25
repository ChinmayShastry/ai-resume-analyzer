import streamlit as st
import plotly.express as px
import pandas as pd
import re

from services.parser import extract_text_from_pdf
from services.skills import extract_skills
from services.gap_analysis import compute_gap
from services.embeddings import compute_similarity
from services.scorer import calculate_score
from services.llm import get_full_analysis
from services.pdf_exporter import generate_resume_pdf
from utils.text_splitter import split_resume_sections


# ---------------- CACHING ----------------
@st.cache_data(max_entries=10)
def cached_extract_text(file_bytes):
    import io
    return extract_text_from_pdf(io.BytesIO(file_bytes))


@st.cache_data(max_entries=10)
def cached_extract_skills(text):
    return extract_skills(text)


@st.cache_data(max_entries=10)
def cached_similarity(resume, jd):
    return compute_similarity(resume, jd)


# ---------------- HIGHLIGHT FUNCTION ----------------
def highlight_missing_skills(text, missing_skills):
    highlighted = text

    for skill in missing_skills:
        pattern = re.compile(rf"\b{re.escape(skill)}\b", re.IGNORECASE)
        highlighted = pattern.sub(
            f"<span style='background-color:#ffcccc; padding:2px'>{skill}</span>",
            highlighted
        )

    return highlighted


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

    try:
        with st.spinner("🧠 AI is analyzing your resume..."):

            resume_text = cached_extract_text(file.getvalue())

            if not resume_text.strip():
                st.error("Could not extract text from PDF")
                st.stop()

            resume_skills = cached_extract_skills(resume_text)
            jd_skills = cached_extract_skills(jd)

            gap = compute_gap(resume_skills, jd_skills)

            similarity = cached_similarity(resume_text, jd)
            score, components = calculate_score(similarity, gap)

            feedback, rewritten = get_full_analysis(resume_text, jd, api_key)

            sections = split_resume_sections(resume_text)

            st.session_state.result = {
                "resume_text": resume_text,
                "gap": gap,
                "score": score,
                "components": components,
                "feedback": feedback,
                "rewritten": rewritten,
                "sections": sections
            }

    except Exception as e:
        st.error("Something went wrong during analysis")
        st.error(str(e))

# ---------------- OUTPUT ----------------
data = st.session_state.result

if data:

    st.markdown("## 📊 Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Score", f"{data['score']}%")
    col2.metric("Matched Skills", len(data["gap"]["matched_skills"]))
    col3.metric("Missing Skills", len(data["gap"]["missing_skills"]))

    # ---------------- SCORE BREAKDOWN ----------------
    st.markdown("## 📊 Score Breakdown")

    comp = data["components"]

    df = pd.DataFrame({
        "Component": ["Skills", "Similarity", "Format"],
        "Score": [
            comp["skills"] * 100,
            comp["similarity"] * 100,
            comp["format"] * 100
        ]
    })

    fig = px.bar(df, x="Component", y="Score", title="Score Contribution")
    st.plotly_chart(fig, use_container_width=True)

    st.caption("Score is calculated based on skills match, semantic similarity, and resume structure.")

    # ---------------- SKILL ANALYSIS ----------------
    st.markdown("## 🧠 Skill Analysis")

    c1, c2 = st.columns(2)

    with c1:
        st.success("Matched Skills")
        st.write(data["gap"]["matched_skills"])

    with c2:
        st.error("Missing Skills")
        st.write(data["gap"]["missing_skills"])

    # ---------------- MISSING SKILLS HIGHLIGHT ----------------
    st.markdown("## 🔍 Missing Skills Highlight")

    missing = data["gap"]["missing_skills"]

    if missing:
        st.warning(f"Consider adding these skills: {', '.join(missing)}")

        highlighted_text = highlight_missing_skills(
            data["resume_text"],
            missing
        )

        st.markdown(highlighted_text, unsafe_allow_html=True)

        # ---------------- SUGGESTIONS ----------------
        st.markdown("## 💡 Suggested Additions")

        for skill in missing:
            st.write(f"- Add experience or project involving **{skill}**")

    else:
        st.success("No missing skills detected 🎉")

    # ---------------- SECTIONS ----------------
    st.markdown("## 📂 Resume Sections")

    for section, content in data["sections"].items():
        st.subheader(section.capitalize())
        st.write(content.strip())

    # ---------------- FEEDBACK ----------------
    st.markdown("## 💬 AI Feedback")
    st.info(data["feedback"])

    # ---------------- REWRITE ----------------
    st.markdown("## ✍️ Improved Resume")
    st.code(data["rewritten"])

    # ---------------- DOWNLOAD ----------------
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

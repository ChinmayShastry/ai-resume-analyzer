# 🚀 AI Resume Analyzer

An AI-powered web application that analyzes a resume against a job description and provides insights to improve it. The tool simulates how an Applicant Tracking System (ATS) evaluates resumes and gives actionable feedback.

**Use This Link** - **https://resume-aianalyzer.streamlit.app/**

## 📌 Features
- 📄 Upload resume (PDF)
- 🧾 Paste job description
- 📊 Resume match score
- 🧠 Skill gap analysis (matched & missing skills)
- 📉 Score breakdown visualization
- 💬 AI-generated feedback
- ✍️ AI resume rewriting
- 🔍 Highlight missing skills in resume
- 📂 Section-wise resume breakdown
- 📥 Download improved resume report (PDF)

## 🧠 How It Works

The system follows a modular pipeline:

### 1. Resume Parsing
Extracts text from PDF using pdfplumber

### 2. Skill Extraction
- Uses predefined skill list
- Applies regex-based matching for accurate detection

### 3. Gap Analysis
Compares resume skills with job description

Outputs:
- Matched skills
- Missing skills
- Match percentage

### 4. Semantic Similarity
- Uses sentence-transformers (MiniLM model)
- Splits resume into chunks
- Computes similarity with job description
- Selects best matching section

### 5. Scoring System

Final score is calculated using weighted components:
- Skills match → 40%
- Semantic similarity → 40%
- Resume structure → 20%

### 6. AI Feedback & Rewrite
Uses **OpenAI API**

Generates:
- Strengths & weaknesses
- Missing skills
- Improvement suggestions
- Improved resume bullet points

### 7. Visualization
Displays score breakdown using Plotly charts

### 8. Resume Highlighting
- Highlights missing skills directly in resume text
- Suggests improvements

## 🏗️ Project Structure

ai-resume-analyzer/
│
├── app.py                 # Streamlit UI
├── config.py              # Config & prompts
├── requirements.txt
│
├── services/
│   ├── parser.py          # PDF text extraction
│   ├── skills.py          # Skill extraction
│   ├── gap_analysis.py    # Skill comparison
│   ├── embeddings.py      # Semantic similarity
│   ├── scorer.py          # Score calculation
│   ├── llm.py             # AI feedback + rewrite
│   ├── pdf_exporter.py    # PDF report generation
│
├── utils/
│   └── text_splitter.py   # Resume section detection

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/your-username/ai-resume-analyzer.git  
cd ai-resume-analyzer

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
streamlit run app.py

## 🔑 API Key Setup

This app uses OpenAI API for AI features.

Enter your API key in the app UI:
- 🔑 OpenAI API Key

## 🧪 Example Workflow

1. Upload your resume (PDF)
2. Paste a job description
3. Click Analyze Resume
4. View:
   - Score
   - Skill gaps
   - AI feedback
   - Improved resume
5. Download report

## 📊 Tech Stack

- Frontend: Streamlit
- Visualization: Plotly
- NLP: sentence-transformers
- ML: scikit-learn
- LLM: OpenAI API
- PDF Processing: pdfplumber, reportlab

## ⚡ Optimizations

- Caching for faster performance
- Chunk-based similarity for better accuracy
- Combined LLM calls to reduce API cost
- Error handling for robustness

## ⚠️ Limitations

- Skill extraction is rule-based (can miss variations)
- Section detection is heuristic-based
- Requires OpenAI API key for AI features

## 🚀 Future Improvements

- Add free mode (without API key)
- Support multiple LLM providers (Gemini, Grok)
- Improve skill extraction using NLP models
- Resume ranking against multiple job descriptions
- Better PDF formatting
- Deployment on cloud

## 🎯 Use Cases

- Job seekers improving resumes
- Students preparing for placements
- Resume screening simulation
- ATS optimization

## 🤝 Contributing

Feel free to fork the repo and improve it.


## ⭐ Final Note

This project combines:
- Rule-based logic
- Machine learning
- Generative AI

to create a practical and intelligent resume optimization tool.

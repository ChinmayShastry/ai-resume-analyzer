from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from io import BytesIO


def generate_resume_pdf(original_resume: str, improved_resume: str, score: float):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    styles = getSampleStyleSheet()
    elements = []

    # ---------------- TITLE ----------------
    elements.append(Paragraph("AI Optimized Resume Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # ---------------- SCORE ----------------
    elements.append(Paragraph(f"Resume Match Score: {score:.2f}%", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # ---------------- ORIGINAL RESUME ----------------
    elements.append(Paragraph("Original Resume", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    for line in original_resume.split("\n"):
        line = line.strip()

        if not line:
            elements.append(Spacer(1, 6))
            continue

        # Bullet handling
        if line.startswith("-"):
            elements.append(Paragraph(f"• {line[1:].strip()}", styles["Normal"]))
        else:
            elements.append(Paragraph(line, styles["Normal"]))

        elements.append(Spacer(1, 4))

    elements.append(Spacer(1, 12))

    # ---------------- IMPROVED RESUME ----------------
    elements.append(Paragraph("AI Improved Resume", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    for line in improved_resume.split("\n"):
        line = line.strip()

        if not line:
            elements.append(Spacer(1, 8))
            continue

        # Section headers (ALL CAPS)
        if line.isupper():
            elements.append(Paragraph(line, styles["Heading2"]))

        # Bullet points
        elif line.startswith("-"):
            elements.append(Paragraph(f"• {line[1:].strip()}", styles["Normal"]))

        # Normal text
        else:
            elements.append(Paragraph(line, styles["Normal"]))

        elements.append(Spacer(1, 6))

    # ---------------- BUILD PDF ----------------
    doc.build(elements)

    buffer.seek(0)
    return buffer

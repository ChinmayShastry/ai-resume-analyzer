from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO


def generate_resume_pdf(original_resume: str, improved_resume: str, score: float):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=50,
        rightMargin=50,
        topMargin=50,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # ---------------- CUSTOM STYLES ----------------
    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Title"],
        fontSize=18,
        leading=22,
        spaceAfter=10
    )

    section_style = ParagraphStyle(
        name="SectionStyle",
        parent=styles["Heading2"],
        fontSize=13,
        textColor=colors.black,
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        name="BodyStyle",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=14
    )

    bullet_style = ParagraphStyle(
        name="BulletStyle",
        parent=styles["Normal"],
        fontSize=10.5,
        leftIndent=10,
        leading=14
    )

    elements = []

    # ---------------- HEADER ----------------
    elements.append(Paragraph("AI Improved Resume", title_style))
    elements.append(Paragraph(f"Match Score: {score:.2f}%", body_style))
    elements.append(Spacer(1, 12))

    # ---------------- IMPROVED RESUME ONLY ----------------
    # (Cleaner output—no need to show original in final doc)

    for line in improved_resume.split("\n"):
        line = line.strip()

        if not line:
            elements.append(Spacer(1, 6))
            continue

        # SECTION HEADINGS (ALL CAPS)
        if line.isupper():
            elements.append(Paragraph(line, section_style))

        # BULLET POINTS
        elif line.startswith("-"):
            elements.append(
                Paragraph(f"• {line[1:].strip()}", bullet_style)
            )

        # NORMAL TEXT
        else:
            elements.append(Paragraph(line, body_style))

    # ---------------- BUILD ----------------
    doc.build(elements)

    buffer.seek(0)
    return buffer

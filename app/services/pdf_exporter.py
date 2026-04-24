from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_resume_pdf(original_resume: str, improved_resume: str, score: float):

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    width, height = letter
    y = height - 50

    def new_page_if_needed():
        nonlocal y
        if y < 60:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = height - 50

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "AI Optimized Resume Report")
    y -= 40

    # Score
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Resume Match Score: {score:.2f}%")
    y -= 30

    # Divider
    pdf.line(50, y, 550, y)
    y -= 30

    # Original Resume Section
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Original Resume:")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for line in original_resume.split("\n"):
        new_page_if_needed()
        pdf.drawString(50, y, line[:100])
        y -= 15

    y -= 20

    # Improved Resume Section
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "AI Improved Resume:")
    y -= 20

    pdf.setFont("Helvetica", 10)
    for line in improved_resume.split("\n"):
        new_page_if_needed()
        pdf.drawString(50, y, line[:100])
        y -= 15

    pdf.save()
    buffer.seek(0)

    return buffer
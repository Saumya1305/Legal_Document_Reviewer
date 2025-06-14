from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def create_pdf(summary, clauses, score, missing_clauses):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    y = height - 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, "LexAI - Document Analysis Report")

    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(40, y, "Summary:")
    y -= 20
    for line in summary.split('. '):
        c.drawString(60, y, f"- {line.strip()}")
        y -= 20

    y -= 10
    c.drawString(40, y, "Clause Detection:")
    y -= 20
    for clause, found in clauses.items():
        status = "Present" if found else "Missing"
        c.drawString(60, y, f"- {clause}: {status}")
        y -= 20

    y -= 10
    c.drawString(40, y, f"Risk Score: {score} / 100")
    y -= 20
    if missing_clauses:
        c.drawString(40, y, "Missing Clauses:")
        y -= 20
        for clause in missing_clauses:
            c.drawString(60, y, f"- {clause}")
            y -= 20
    else:
        c.drawString(40, y, "All clauses are present.")
        y -= 20

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

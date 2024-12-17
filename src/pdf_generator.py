import time
import os
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import tkinter.messagebox as messagebox

def generate_pdf(report, root=None):
    html_report = markdown.markdown(report)

    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    unique_filename = f"report_{timestamp}.pdf"
    pdf_path = os.path.join("reports", unique_filename)

    document = SimpleDocTemplate(pdf_path, pagesize=letter)

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    
    content = []
    content.append(Paragraph(html_report, normal_style))
    document.build(content)

    if root:
        messagebox.showinfo("PDF Generation", f"PDF saved as {pdf_path}")
    else:
        print(f"PDF saved as {pdf_path}")
import time
import os
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import tkinter.messagebox as messagebox
from io import BytesIO

def generate_bar_chart(energy_footprint, waste_footprint, business_travel_footprint):
    labels = ['Energy Footprint', 'Waste Footprint', 'Business Travel Footprint']
    values = [energy_footprint, waste_footprint, business_travel_footprint]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['#ff9999', '#66b3ff', '#99ff99'])

    ax.set_ylabel('CO2 Emissions (tons per year)')
    ax.set_title('Carbon Footprint Breakdown')

    bar_chart_buffer = BytesIO()
    plt.savefig(bar_chart_buffer, format='png', bbox_inches='tight')
    plt.close()

    bar_chart_buffer.seek(0)

    return bar_chart_buffer

def markdown_to_pdf_content(report):
    lines = report.split("\n")
    content = []

    styles = getSampleStyleSheet()
    heading_style = ParagraphStyle(name="HeadingStyle", fontSize=18, alignment=1, spaceAfter=12, fontName="Helvetica-Bold")
    normal_style = styles["Normal"]
    bold_style = ParagraphStyle(name="BoldStyle", fontSize=12, alignment=0, fontName="Helvetica-Bold")

    for line in lines:
        if line.startswith("# "):
            content.append(Paragraph(f"<font size=16><b>{line[2:]}</b></font>", heading_style))
        elif line.startswith("### "):
            content.append(Paragraph(f"<font size=12><b>{line[3:]}</b></font>", heading_style))
        elif line.startswith("- "):
            content.append(Paragraph(f"<font size=12>{line[2:]}</font>", normal_style))
        elif "**" in line:
            parts = line.split("**")
            text = f"<font size=12>{parts[0]}<b>{parts[1]}</b>{parts[2]}</font>"
            content.append(Paragraph(text, normal_style))
        else:
            content.append(Paragraph(f"<font size=12>{line}</font>", normal_style))

        content.append(Spacer(1, 12))

    return content

def generate_pdf(report, energy_footprint, waste_footprint, business_travel_footprint, root=None):
    if not report.strip():
        if root:
            messagebox.showwarning("Empty Report", "No data to generate a PDF report.")
        else:
            print("No data to generate a report.")
        return

    bar_chart_buffer = generate_bar_chart(energy_footprint, waste_footprint, business_travel_footprint)

    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    unique_filename = f"report_{timestamp}.pdf"
    pdf_path = os.path.join("reports", unique_filename)

    document = SimpleDocTemplate(pdf_path, pagesize=letter)

    content = markdown_to_pdf_content(report)

    content.append(Spacer(1, 12))
    content.append(Image(bar_chart_buffer, width=400, height=300))

    document.build(content)

    bar_chart_buffer.close()

    if root:
        messagebox.showinfo("PDF Generation", f"PDF saved in the reports folder as {pdf_path}")
    else:
        print(f"PDF saved in the reports folder as {pdf_path}")
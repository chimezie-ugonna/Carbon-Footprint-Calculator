import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

def generate_report(energy_footprint, waste_footprint, business_travel_footprint):
    prompt = f"""
Calculate the carbon footprint based on the following:
- Energy Footprint: {energy_footprint} tons CO2 per year.
- Waste Footprint: {waste_footprint} tons CO2 per year.
- Business Travel Footprint: {business_travel_footprint} tons CO2 per year.

Provide a comprehensive and user-friendly report with:
1. A professional structure, including sections for energy, waste, and business travel, with detailed headings and subheadings.
2. Specific, actionable strategies for reducing carbon emissions in each category, tailored to both urban and corporate contexts.
3. References to multiple reliable data sources, fully detailed and appropriately linked.
4. A visually appealing markdown layout with clear headings, bullet points, and tables where relevant. Suggest data visualization ideas (e.g., pie charts, bar graphs) to present the findings effectively.
5. Quantify the potential reduction in carbon emissions for each suggested action, explaining the methodology briefly.
6. A concluding section summarizing key insights and prioritizing the most impactful measures.

Ensure the content is polished, easy to understand, and uses professional terminology to engage an academic audience.
"""
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text
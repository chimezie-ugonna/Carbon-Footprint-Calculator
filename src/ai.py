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
Provide a professional, user-friendly report with the following structure:
1. **Key Footprint Values**:
   - **Energy Footprint:** {energy_footprint} tons CO2 per year.
   - **Waste Footprint:** {waste_footprint} tons CO2 per year.
   - **Business Travel Footprint:** {business_travel_footprint} tons CO2 per year.
2. **Footprint Breakdown**:
   For each category (Energy, Waste, Business Travel):
   - Identify key sources of emissions.
   - Provide **reduction strategies**, supported by **real-world examples** and **credible sources** (e.g., industry case studies, government reports).
   - Quantify the potential reductions for each strategy (e.g., "20% reduction through renewable energy adoption as demonstrated by Company X").
   - Suggest next steps for a more detailed audit if needed (e.g., energy audit).
3. **Summary & Recommendations**:
   - Prioritize the most impactful strategies for each category.
   - Offer a concise, actionable recommendation based on real-world results (e.g., "Transitioning to renewable energy reduced emissions by 40% in Company X within 2 years").
Use simple language, avoid nested markdown, and ensure the report is clear and professional. Include links to reputable sources when appropriate.
"""
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    return response.text
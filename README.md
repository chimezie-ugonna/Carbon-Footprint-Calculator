# Carbon Footprint Calculator

## Overview
The **Carbon Footprint Calculator** is a Python-based application designed to estimate the carbon footprint of an individual or entity's energy consumption, waste generation, and business travel. The app calculates the carbon emissions from user inputs and generates a professional and AI powered report with suggestions for reducing these emissions.

---

## Features

- **Energy Footprint Calculation**: Estimates carbon emissions based on electricity, gas, and fuel bills.
- **Waste Footprint Calculation**: Calculates emissions from waste generation, factoring in recycling.
- **Business Travel Footprint**: Computes the carbon footprint based on kilometers traveled and fuel efficiency.
- **AI-Generated Report**: Uses AI to generate a professional, user-friendly report with actionable reduction strategies.
- **PDF Generation**: Converts the generated report into a well-formatted PDF, complete with a carbon footprint barchart.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chimezie-ugonna/Carbon-Footprint-Calculator.git
   ```
   
2. Navigate to the project folder:

   ```bash
   cd Carbon-Footprint-Calculator
   ```

3.	Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    
## Set Up Google API Key

1. Visit the [Google API Key Generator](https://aistudio.google.com/app/u/1/apikey?_gl=1*qh6gbs*_ga*MTc3MTg1MzU1My4xNzM0NDE5MTcy*_ga_P1DBVKWT6V*MTczNDUxODEwMy4zLjEuMTczNDUxODExNC40OS4wLjE4NTkzMDc3MDA.&pli=1).
2. Create an API key by following the steps on the site.
3. Copy the created API key.
4. Create a `.env` file in the project root directory and add the following line:
   
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

### 1. Calculate Carbon Footprints
Use the functions in `calculations.py` to calculate energy, waste, and business travel footprints.  
Example:
```python
energy_footprint = calculate_energy_footprint(electricity_bill, gas_bill, fuel_bill)
waste_footprint = calculate_waste_footprint(waste_generated, recycling_percentage)
business_travel_footprint = calculate_business_travel_footprint(km_travel, fuel_efficiency)
```

### 2.	Generate Report
Use the `generate_report()` function in `ai.py` to generate a detailed, AI-driven report.

```python
report = generate_report(energy_footprint, waste_footprint, business_travel_footprint)
```

### 3.	Generate PDF
Use the `generate_pdf()` function in `pdf_generator.py` to convert the generated report into a PDF and store it in the `reports` folder.

```python
generate_pdf(report, energy_footprint, waste_footprint, business_travel_footprint)
```

## Example
Here’s an example of how to use the application:

```python
from calculations import calculate_energy_footprint, calculate_waste_footprint, calculate_business_travel_footprint
from ai import generate_report
from pdf_generator import generate_pdf

# Sample inputs
electricity_bill = 100  # Monthly bill in local currency
gas_bill = 50
fuel_bill = 30
waste_generated = 200  # Monthly waste in kg
recycling_percentage = 30
km_travel = 500  # Monthly business travel in km
fuel_efficiency = 15  # Fuel efficiency in km per liter

# Calculate footprints
energy_footprint = calculate_energy_footprint(electricity_bill, gas_bill, fuel_bill)
waste_footprint = calculate_waste_footprint(waste_generated, recycling_percentage)
business_travel_footprint = calculate_business_travel_footprint(km_travel, fuel_efficiency)

# Generate the report
report = generate_report(energy_footprint, waste_footprint, business_travel_footprint)

# Generate the PDF
generate_pdf(report, energy_footprint, waste_footprint, business_travel_footprint)
```

### Technologies Used

- **Python 3.13.1**: Core language for the application.
- **Google Generative AI API**: For generating AI-powered reports.
- **Matplotlib**: For generating data visualizations such as bar charts.
- **ReportLab**: For creating and formatting PDF documents.

### Contributing

If you’d like to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with clear descriptions and test cases.

### License

This project is for academic purposes only. No formal license is provided, and usage is restricted to the course requirements and evaluation by the instructor.

### Acknowledgments

- **Google Generative AI**: For providing advanced AI capabilities to generate detailed reports.
- **Matplotlib**: For enabling data visualizations to illustrate carbon footprints.
- **ReportLab**: For making PDF generation seamless and professional.
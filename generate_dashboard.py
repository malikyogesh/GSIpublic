import os
import google.generativeai as genai # Or import openai
from datetime import datetime

# 1. Setup API (Get key from aistudio.google.com)
genai.configure(api_key=os.environ[""])

# 2. Define the Prompt
current_date = datetime.now().strftime("%Y-%m-%d")
prompt = f"""
You are an expert IT analyst. Today is {current_date}.
Research the latest news for HCLTech, TCS, Wipro, and Infosys.
Then, generate a SINGLE, complete, standalone HTML file containing an interactive dashboard.
The dashboard must have:
- A professional CSS design (corporate dark/light theme).
- Tabs for 'Executive Summary', 'Company Deep Dives', 'Comparison', and '2026 Forecast'.
- Dummy data or extrapolated trends based on your knowledge up to today.
- A JavaScript Chart.js visualization for market sentiment.
Output ONLY the raw HTML code. Do not use markdown blocks.
"""

# 3. Call the AI
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(prompt)
html_content = response.text

# Clean up markdown formatting if the AI adds it
html_content = html_content.replace("```html", "").replace("```", "")

# 4. Save to file
with open("index.html", "w", encoding='utf-8') as f:
    f.write(html_content)

print("Dashboard updated successfully!")

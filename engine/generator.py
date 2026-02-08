import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def get_client():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY not found in environment.")
    return genai.Client(api_key=key)

def generate_corep_output(query: str, scenario: str, retrieved_rules: list) -> dict:
    client = get_client()

    rules_text = "\n".join(retrieved_rules)

    system_prompt = """
You are a regulatory reporting assistant for COREP C 01.00 (Own Funds).

Rules:
- Use ONLY the provided regulatory text.
- Return ONLY valid JSON.
- No explanations outside JSON.
- Include rule references for each field.
"""

    user_prompt = f"""
User Question:
{query}

Scenario:
{scenario}

Regulatory Text:
{rules_text}

Return JSON in this format:

{{
  "template_id": "COREP_C_01_00",
  "reporting_entity": "Example Bank",
  "reporting_date": "2025-12-31",
  "fields": [
    {{
      "code": "010",
      "field_name": "CET1 Capital",
      "value": 0,
      "unit": "GBP",
      "rule_references": [],
      "notes": ""
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{system_prompt}\n\n{user_prompt}",
        config=types.GenerateContentConfig(temperature=0.2)
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)

"""
SAP ERP Recommendation System — India Edition
------------------------------------------------
Takes company/business info (India-specific: GST, multi-state ops, turnover
in INR) via a web form, sends it to Gemini with a structured prompt, and
returns a proper SAP ERP RFP recommendation:
  1. The right SAP product tier (Business One / S/4HANA Cloud / On-Premise etc.)
  2. Reasoning
  3. Recommended SAP modules WITH fit scores (used to draw a small dashboard)
  4. Estimated cost in INR (Lakhs) broken into license / implementation / AMC
  5. Implementation timeline
  6. India-compliance notes (GST, e-invoicing, TDS/TCS)
  7. A proper RFP outline

Run:
    python app.py
Then open http://127.0.0.1:5000
"""

import os
import json
import time
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# ----------------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------------
# Get a free Gemini API key at: https://aistudio.google.com/apikey
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:generateContent"
)


# ----------------------------------------------------------------------
# CORE LOGIC: Build the prompt + call Gemini
# ----------------------------------------------------------------------
def build_prompt(data: dict) -> str:
    """Turn the submitted form data into a structured prompt for Gemini."""
    return f"""
You are a senior SAP ERP implementation consultant based in India, specializing
in writing RFP (Request for Proposal) recommendations for Indian businesses.

Analyze the following Indian company's profile and recommend the SINGLE most
suitable SAP product from this list ONLY:
- SAP Business One (best for small businesses, <100 employees, single/few locations)
- SAP Business ByDesign (mid-market, growing multi-location companies)
- SAP S/4HANA Cloud, Public Edition (mid-to-large, standardized processes, fast rollout)
- SAP S/4HANA Cloud, Private Edition (large enterprises needing customization)
- SAP S/4HANA On-Premise (large enterprises with complex/regulated requirements,
  data residency needs, or heavy customization)

All cost estimates MUST be in Indian Rupees, expressed in Lakhs (1 Lakh = ₹100,000).
Give realistic indicative ranges for the Indian market — do not use USD anywhere.

COMPANY PROFILE (India):
- Industry: {data['industry']}
- Company size (employees): {data['company_size']}
- Annual turnover: {data['turnover']}
- Number of business locations / states of operation: {data['locations']}
- GST registered: {data['gst_registered']}
- Involved in exports/imports: {data['export_import']}
- Current systems in use: {data['current_systems']}
- Key business goals: {data['goals']}
- Main pain points / challenges: {data['pain_points']}
- ERP budget: {data['budget']}
- Preferred deployment (Cloud / On-Premise / Hybrid / No preference): {data['deployment']}

Consider Indian regulatory/compliance needs specifically: GST (multi-GSTIN if
multiple states), e-invoicing (IRN generation), e-way bill, TDS/TCS automation,
and any industry-specific compliance relevant to their sector.

Respond ONLY in the following strict JSON format, no markdown, no extra text,
no comments — valid JSON only:

{{
  "recommended_sap_product": "exact SAP product name from the list above",
  "confidence_score": 85,
  "reasoning": "3-5 sentences explaining why this SAP product fits this company, referencing their industry, size, and India-specific needs",
  "recommended_modules": [
    {{"name": "SAP module name (e.g. Finance & Controlling - FICO)", "suitability_score": 90, "reason": "1-line reason"}},
    {{"name": "module name", "suitability_score": 80, "reason": "1-line reason"}},
    {{"name": "module name", "suitability_score": 75, "reason": "1-line reason"}},
    {{"name": "module name", "suitability_score": 70, "reason": "1-line reason"}},
    {{"name": "module name", "suitability_score": 65, "reason": "1-line reason"}}
  ],
  "estimated_cost_inr_lakhs": {{
    "licensing_or_subscription": 12,
    "implementation_services": 18,
    "annual_maintenance": 4
  }},
  "implementation_timeline_months": 6,
  "alternative_option": "name of a second-best SAP product tier and 1-line reason",
  "india_compliance_notes": "2-3 sentences on GST/e-invoicing/TDS-TCS/e-way bill relevance for this company specifically",
  "rfp_outline": [
    "Section 1 title: 1-line description",
    "Section 2 title: 1-line description",
    "Section 3 title: 1-line description",
    "Section 4 title: 1-line description",
    "Section 5 title: 1-line description",
    "Section 6 title: 1-line description",
    "Section 7 title: 1-line description"
  ]
}}

Numbers must be plain numbers (no currency symbols, no commas) since they will
be used to draw charts. confidence_score and suitability_score must be integers
between 0 and 100.
"""


def call_gemini(prompt: str, max_retries: int = 2) -> dict:
    """Calls the Gemini API and returns the parsed JSON recommendation.
    Retries once on 429 (rate limit) using the server's suggested delay."""
    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Get a free key at "
            "https://aistudio.google.com/apikey and set it as an "
            "environment variable before running the app."
        )

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.4,
            "response_mime_type": "application/json",
        },
    }

    last_error = None
    for attempt in range(max_retries + 1):
        resp = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=60,
        )

        if resp.status_code == 200:
            result = resp.json()
            try:
                text_output = result["candidates"][0]["content"]["parts"][0]["text"]
            except (KeyError, IndexError) as e:
                raise RuntimeError(f"Unexpected Gemini response format: {result}") from e
            text_output = text_output.strip().strip("```json").strip("```").strip()
            return json.loads(text_output)

        if resp.status_code == 429 and attempt < max_retries:
            wait_seconds = 5
            try:
                err_json = resp.json()
                for detail in err_json.get("error", {}).get("details", []):
                    if detail.get("@type", "").endswith("RetryInfo"):
                        delay = detail.get("retryDelay", "5s").rstrip("s")
                        wait_seconds = float(delay) + 1
            except Exception:
                pass
            time.sleep(min(wait_seconds, 40))
            last_error = f"Gemini API error ({resp.status_code}): {resp.text}"
            continue

        raise RuntimeError(f"Gemini API error ({resp.status_code}): {resp.text}")

    raise RuntimeError(last_error or "Gemini API request failed after retries.")


# ----------------------------------------------------------------------
# ROUTES
# ----------------------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    form_data = {
        "industry": request.form.get("industry", "").strip(),
        "company_size": request.form.get("company_size", "").strip(),
        "turnover": request.form.get("turnover", "").strip(),
        "locations": request.form.get("locations", "").strip(),
        "gst_registered": request.form.get("gst_registered", "").strip(),
        "export_import": request.form.get("export_import", "").strip(),
        "current_systems": request.form.get("current_systems", "").strip(),
        "goals": request.form.get("goals", "").strip(),
        "pain_points": request.form.get("pain_points", "").strip(),
        "budget": request.form.get("budget", "").strip(),
        "deployment": request.form.get("deployment", "No preference").strip(),
    }

    error = None
    recommendation = None

    try:
        prompt = build_prompt(form_data)
        recommendation = call_gemini(prompt)

        # Precompute total cost for display / charting
        costs = recommendation.get("estimated_cost_inr_lakhs", {})
        recommendation["total_cost_inr_lakhs"] = round(
            sum(float(v) for v in costs.values()), 2
        )
    except Exception as e:
        error = str(e)

    return render_template(
        "result.html",
        form_data=form_data,
        recommendation=recommendation,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

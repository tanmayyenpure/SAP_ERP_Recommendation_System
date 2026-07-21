# SAP ERP Recommendation System — India Edition

A working web app that gives Indian businesses a proper SAP ERP RFP
recommendation using Gemini (free tier), with a small Power BI–style
dashboard on the results page.

## What it does
1. You fill a form describing the company: industry, size, turnover (in ₹),
   number of locations/states, GST registration status, exports/imports,
   current systems, goals, pain points, budget (₹), deployment preference.
2. Gemini analyzes it and returns:
   - The right **SAP product tier** — SAP Business One, SAP Business
     ByDesign, SAP S/4HANA Cloud (Public or Private Edition), or SAP
     S/4HANA On-Premise
   - **Recommended SAP modules** with fit scores (FICO, SD, MM, PP, QM, etc.)
   - **Estimated cost in ₹ Lakhs**, broken into licensing, implementation,
     and annual maintenance
   - **Implementation timeline**
   - **India compliance notes** — GST/multi-GSTIN, e-invoicing (IRN),
     e-way bill, TDS/TCS
   - A **starter RFP outline**
3. The results page renders a small dashboard: KPI cards + a bar chart
   of module fit scores + a doughnut chart of the cost breakdown
   (via Chart.js, loaded client-side — no extra setup needed).

## 1. Get a free Gemini API key
1. Go to https://aistudio.google.com/apikey
2. Sign in with a Google account and create an API key.

> **Note on free-tier quota errors (HTTP 429 / RESOURCE_EXHAUSTED):**
> Google tightened Gemini's free tier in Dec 2025. If you see `limit: 0`
> errors, try: (a) a different model via `GEMINI_MODEL` (e.g.
> `gemini-2.5-flash`, `gemini-flash-lite-latest`), (b) generating a fresh
> key in a **new** AI Studio project, or (c) enabling billing on the
> project (you still won't be charged within the free allotment).
> The app automatically retries once on a 429 using Google's suggested
> retry delay.

## 2. Install dependencies
```bash
cd erp-recommender
python -m venv venv

# macOS/Linux:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (Git Bash / MINGW64):
source venv/Scripts/activate

pip install -r requirements.txt
```

## 3. Set your API key
```bash
export GEMINI_API_KEY="your_key_here"          # PowerShell: $env:GEMINI_API_KEY="your_key_here"
export GEMINI_MODEL="gemini-2.5-flash"          # optional, this is the default
```

## 4. Run the app
```bash
python app.py
```
Open **http://127.0.0.1:5000**

## Project structure
```
erp-recommender/
├── app.py                # Flask app + Gemini API integration + retry logic
├── requirements.txt
├── templates/
│   ├── index.html         # India-specific input form
│   └── result.html        # Recommendation + dashboard (Chart.js)
└── static/
    └── style.css
```

## Notes
- All cost figures are AI-generated **indicative estimates** in ₹ Lakhs —
  not a quote. Useful for budgeting conversations, not a final contract
  figure.
- No database — nothing is saved between requests (by design, for now).
- Charts run entirely in the browser via Chart.js (CDN) — no extra backend
  work needed.

## Natural next steps (when you're ready to go further)
- Export the full recommendation + RFP as a downloadable Word/PDF document
- Save recommendation history to a database
- Compare 2–3 SAP product tiers side-by-side
- Let users upload existing financial/inventory data for deeper analysis

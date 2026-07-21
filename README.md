# 💼 SAP ERP Recommendation System

<p align="center">
  <strong>AI-powered SAP ERP Recommendation Platform for Indian Businesses</strong>
</p>

<p align="center">
  This application uses <b>Google Gemini AI</b> to analyze business requirements and recommend the most suitable SAP ERP solution along with SAP modules, estimated implementation cost, deployment timeline, compliance insights, and a starter RFP.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_AI-4285F4?style=for-the-badge&logo=google)
![SAP](https://img.shields.io/badge/SAP-ERP-0FAAFF?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

# 🌐 About the Project

SAP ERP Recommendation System is an AI-powered web application that helps businesses identify the most suitable SAP ERP solution based on their business requirements.

The system analyzes company information using **Google Gemini AI** and provides intelligent recommendations, including the best SAP ERP product, suitable SAP modules, estimated implementation cost, deployment timeline, India-specific compliance considerations, and a starter Request for Proposal (RFP).

---

# ✨ Key Features

- 🤖 AI-powered SAP ERP recommendations
- 🏢 Business profile analysis
- 📊 Intelligent SAP product selection
- 📦 SAP module recommendations
- 💰 Estimated implementation cost
- 📅 Deployment timeline
- 🇮🇳 India-specific compliance guidance
- 📄 Starter RFP generation
- 📈 Interactive dashboard with charts

---

# 🏢 SAP Solutions

The application recommends the most suitable ERP solution from:

- SAP Business One
- SAP Business ByDesign
- SAP S/4HANA Cloud (Public Edition)
- SAP S/4HANA Cloud (Private Edition)
- SAP S/4HANA On-Premise

---

# 📝 Business Inputs

The recommendation is generated using:

- Industry
- Company Size
- Annual Turnover
- Business Locations
- GST Registration
- Import & Export Information
- Existing Software
- Business Goals
- Business Challenges
- Budget
- Preferred Deployment

---

# 🤖 AI Recommendations

After analyzing the business profile, the system provides:

- ✅ Best SAP ERP Solution
- ✅ Recommended SAP Modules
- ✅ Module Fit Scores
- ✅ Estimated Implementation Cost
- ✅ Cost Breakdown
- ✅ Deployment Timeline
- ✅ India Compliance Notes
- ✅ Starter RFP Outline

---

# 📸 Project Preview

### Home Page

> Add your homepage screenshot here.

```
screenshots/home.png
```

### Recommendation Dashboard

> Add your dashboard screenshot here.

```
screenshots/dashboard.png
```

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | HTML5, CSS3, Jinja2 |
| Backend | Python, Flask |
| AI | Google Gemini API |
| Charts | Chart.js |
| Language | Python |

---

# 🏗️ System Design

```text
                   User
                     │
                     ▼
        Business Details Form
                     │
                     ▼
             Flask Backend
                     │
                     ▼
          Google Gemini AI API
                     │
                     ▼
      SAP ERP Recommendation Engine
                     │
                     ▼
      Interactive Recommendation Dashboard
```

---

# 📂 Directory Structure

```text
SAP_ERP_Recommendation_System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── result.html
```

---

# ⚡ Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/tanmayyenpure/SAP_ERP_Recommendation_System.git
```

## 2️⃣ Navigate to the Project Folder

```bash
cd SAP_ERP_Recommendation_System
```

## 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Configure Gemini API Key

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### Linux / macOS

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

---

## 6️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🔄 Application Workflow

```text
User enters business details
            │
            ▼
Flask processes the request
            │
            ▼
Google Gemini AI analyzes the data
            │
            ▼
AI generates SAP ERP recommendations
            │
            ▼
Dashboard displays results with charts
```

---

# 💡 Future Improvements

- 📄 Export recommendations as PDF
- 📑 Export reports in Word format
- 🗄️ Database integration
- 🔐 User authentication
- 📜 Recommendation history
- 🌍 Multi-language support
- ⚖️ Compare multiple SAP ERP solutions

---

# 👨‍💻 Developer

**Tanmay Yenpure**

🎓 Computer Engineering Student  
🤖 AI & Machine Learning Enthusiast  
💻 Full Stack Developer

**GitHub:** https://github.com/tanmayyenpure

---

# 🌟 Show Your Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

---

# 📜 License

This project is licensed under the **MIT License**.

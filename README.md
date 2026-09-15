# 🚚 SmartLogi AI — Supply Chain Disruption Assistant & Fleet Optimizer

> An AI-assisted logistics dashboard for monitoring fleet utilization, identifying shipment disruption risk, and generating fleet reallocation recommendations.

---

## 👥 Team

| Field | Value |
|---|---|
| Team Name | **SmartLogi AI** |
| Track | **AI** |
| Team Lead | **vivek sarvaiya ** |
| Members | **Devanshi Sakariya , Urvashi Chhatbar, Manan Thakar * |

> Replace the bracketed contact/team information before final submission.

## 🎯 Problem Statement

Logistics managers must continuously monitor vehicle capacity, shipment status, route disruptions, and delivery deadlines. Delays, overloaded vehicles, underutilized fleet capacity, traffic, weather, and route problems can increase delivery risk and operating cost, while manual analysis makes it difficult to react quickly.

## 💡 Solution

**SmartLogi AI** provides a logistics command center that combines fleet and shipment dashboards with an AI-assisted risk engine and fleet optimizer. It identifies high-risk shipments, evaluates disruption conditions, highlights underutilized vehicles, and recommends reallocating shipments to better-suited vehicles.

The current project includes a local demonstration data layer and an integration-ready service for IBM watsonx.ai and IBM Cloudant, with fallback behavior when cloud credentials are unavailable.

## ✨ Key Features

- **Fleet Command Center:** Dashboard for vehicles, active shipments, risk, disruptions, utilization, and fleet locations.
- **Disruption Risk Analysis:** Calculates risk scores and risk levels from traffic, weather, vehicle problems, tight deadlines, and blocked routes.
- **AI Fleet Optimizer:** Produces shipment-to-vehicle reassignment recommendations and compares estimated fleet utilization before and after optimization.
- **AI Logistics Assistant:** Chat-style interface for asking about high-risk shipments and fleet underutilization.
- **Analytics & Tracking:** Fleet utilization charts, shipment analytics, and a Gujarat-focused map view using Leaflet.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Languages | Python, HTML5, CSS3, JavaScript |
| Frameworks | Flask, Bootstrap 5 |
| IBM Technologies | IBM watsonx.ai integration, IBM Cloudant integration-ready configuration |
| Databases | JSON demonstration dataset; Cloudant integration-ready |
| Other | Chart.js, Leaflet, Flask-CORS, python-dotenv |

## 📁 Repository Structure

```text
bob-ai-hackathon-supplyguard-ai/
├── src/
│   ├── backend/
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── data/seed_data.json
│   │   └── services/
│   │       ├── risk_engine.py
│   │       └── watsonx_service.py
│   ├── frontend/
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── fleet.html
│   │   ├── shipments.html
│   │   ├── disruptions.html
│   │   ├── optimizer.html
│   │   ├── ai-assistant.html
│   │   ├── analytics.html
│   │   └── css/style.css
│   ├── requirements.txt
│   └── .env.example
├── docs/
│   ├── problem-statement.md
│   ├── solution-overview.md
│   ├── architecture.md
│   └── setup-guide.md
├── demo/
│   ├── screenshots/
│   ├── demo-video.mp4
│   ├── demo-video-link.txt
│   └── live-demo-url.txt
├── presentation/
│   └── README.md
├── .gitignore
├── README.md
└── submission.yaml
```

## ⚡ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Create and activate a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r src/requirements.txt
```

### 4. Configure environment

Copy `src/.env.example` to `src/.env` and add your IBM credentials if you want to connect to watsonx.ai or Cloudant.

```text
WATSONX_API_KEY=
WATSONX_PROJECT_ID=
WATSONX_URL=https://us-south.ml.cloud.ibm.com
CLOUDANT_URL=
CLOUDANT_API_KEY=
```

Do **not** commit `src/.env` or API keys to GitHub.

### 5. Start the Flask backend

```bash
cd src/backend
python app.py
```

The API runs on:

```text
http://localhost:5000
```

### 6. Open the frontend

Open `src/frontend/login.html` in a browser. For a smoother local setup, serve the frontend with a simple static server if your browser blocks local-file requests.

Demo login credentials in the current project are:

```text
Username: admin
Password: admin123
```

## 🖥️ Demo

- **Demo video:** `demo/demo-video.mp4`
- **Hosted video URL:** replace `demo/demo-video-link.txt` with a public YouTube/Loom/Box URL before submission.
- **Live demo:** replace `demo/live-demo-url.txt` if the application is deployed.
- **Screenshots:** `demo/screenshots/`

## ⚠️ Known Limitations

- The current demo primarily uses a local JSON dataset; the Cloudant configuration is integration-ready rather than the default runtime data source.
- The watsonx.ai service has a local fallback when IBM credentials are unavailable.
- Optimization results shown by the demo endpoint are demonstration estimates, not a production-grade mathematical optimization model.
- Live IoT telemetry, live weather/radar feeds, and production authentication are not included in this MVP.
- A hosted demo URL and hosted video URL must be added before final hackathon submission.

## 🏅 What We're Most Proud Of

The strongest part of SmartLogi AI is the **decision-support workflow**: instead of only displaying logistics data, the system connects disruption risk, fleet utilization, and shipment priority into an actionable recommendation. For example, the demo can identify a risky shipment and recommend moving it from an overloaded vehicle to an underutilized vehicle with available capacity.

## IBM Hackathon Submission

This repository follows the structure of the IBM Bob AI Hackathon submission template, including `submission.yaml`, documentation, demo artifacts, source code, and presentation placeholders.

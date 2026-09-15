# Setup Guide

## Requirements

- Python 3.x
- A modern web browser
- Optional IBM watsonx.ai credentials
- Optional IBM Cloudant credentials

## Installation

From the repository root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r src/requirements.txt
```

## Environment Variables

Create `src/.env` from `src/.env.example`:

```text
WATSONX_API_KEY=
WATSONX_PROJECT_ID=
WATSONX_URL=https://us-south.ml.cloud.ibm.com
CLOUDANT_URL=
CLOUDANT_API_KEY=
```

Leave these empty for the local demonstration fallback.

## Start Backend

```bash
cd src/backend
python app.py
```

Backend URL:

```text
http://localhost:5000
```

## Start Frontend

Open `src/frontend/login.html` in a browser. If the browser restricts requests from local files, serve the frontend directory with a simple static HTTP server.

Example:

```bash
cd src/frontend
python -m http.server 5500
```

Then open:

```text
http://localhost:5500/login.html
```

## Demo Credentials

```text
Username: admin
Password: admin123
```

## Troubleshooting

### API connection error
Make sure the Flask server is running on port 5000.

### IBM credentials are not available
The project is designed to use local/demo behavior when IBM cloud credentials are missing.

### CORS/browser issue
Serve the frontend through a local HTTP server instead of opening HTML files directly.

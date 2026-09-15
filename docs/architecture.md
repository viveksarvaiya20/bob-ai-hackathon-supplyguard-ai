# Architecture

## High-Level Architecture

```text
                    +----------------------+
                    |   Web Browser        |
                    | HTML/CSS/JS          |
                    | Bootstrap/Chart.js   |
                    | Leaflet              |
                    +----------+-----------+
                               |
                               | HTTP / JSON
                               v
                    +----------------------+
                    | Flask REST Backend   |
                    | app.py               |
                    +----+------------+----+
                         |            |
             +-----------+            +------------+
             v                                      v
   +-------------------+                  +--------------------+
   | Risk Engine       |                  | AI Service         |
   | risk_engine.py    |                  | watsonx_service.py |
   +---------+---------+                  +---------+----------+
             |                                      |
             v                                      v
   +-------------------+                  +--------------------+
   | Recommendations   |                  | IBM watsonx.ai     |
   +-------------------+                  +--------------------+

                    +----------------------+
                    | Data Layer           |
                    | JSON demo data       |
                    | Cloudant-ready config|
                    +----------------------+
```

## Components

| Component | Responsibility |
|---|---|
| Frontend | Dashboard, fleet, shipments, disruptions, optimizer, analytics, and AI assistant UI |
| Flask API | REST endpoints for dashboard data, vehicles, shipments, disruptions, optimization, chat, and risk analysis |
| Risk Engine | Converts disruption conditions into risk score, risk level, and reasons |
| watsonx Service | Optional IBM watsonx.ai text-generation integration with local fallback |
| Data Layer | Demonstration JSON dataset; Cloudant configuration is available for future/connected deployments |

## API Endpoints

- `GET /api/dashboard`
- `GET /api/vehicles`
- `GET /api/shipments`
- `GET /api/disruptions`
- `POST /api/optimize-fleet`
- `POST /api/ai/chat`
- `POST /api/ai/recommend`
- `POST /api/analyze-risk`

## Security Notes

- API keys must be stored in `.env` and never committed.
- Production deployment should add real authentication, authorization, HTTPS, request validation, and secret management.

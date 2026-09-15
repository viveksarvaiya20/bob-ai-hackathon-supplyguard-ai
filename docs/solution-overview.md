# Solution Overview

SmartLogi AI is a web-based logistics decision-support MVP.

## Core Flow

```text
Fleet + Shipment Data
        |
        v
+-----------------------+
| SmartLogi AI Backend  |
| Flask REST APIs       |
+-----------------------+
        |
        +--------------------+
        |                    |
        v                    v
 Risk Engine          AI Services
 traffic/weather/     watsonx.ai integration
 vehicle/deadline     + local fallback
        |                    |
        +---------+----------+
                  v
          Fleet Optimizer
                  |
                  v
      Recommended Reassignment
                  |
                  v
       Web Dashboard / Assistant
```

## Main Modules

### 1. Dashboard
Shows total vehicles, active shipments, high-risk shipments, active disruptions, utilization, and map-based fleet status.

### 2. Risk Engine
`services/risk_engine.py` calculates a score from conditions such as Heavy Traffic, Rain/Severe Weather, Vehicle Problem, Tight Deadline, and Route Blocked.

### 3. Fleet Optimizer
The demo endpoint compares estimated utilization before/after optimization and provides a recommended reassignment, such as moving shipment S102 from V001 to V004.

### 4. AI Assistant
Provides a conversational interface for logistics questions. When cloud AI is unavailable, the application can use local recommendation logic.

### 5. IBM Integration Layer
`services/watsonx_service.py` is prepared to call IBM watsonx.ai using environment-based credentials. `config.py` also contains Cloudant configuration and fallback flags.

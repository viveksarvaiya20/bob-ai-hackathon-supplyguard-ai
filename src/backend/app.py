from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
import json
import os

app = Flask(__name__)
CORS(app)

# --- MOCK DATABASE ---
DB_FILE = os.path.join(os.path.dirname(__file__), 'data', 'seed_data.json')
def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {"vehicles": [], "shipments": [], "disruptions": [], "routes": []}

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

db = load_db()

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    total_vehicles = len(db["vehicles"])
    active_shipments = len([s for s in db["shipments"] if s["status"] in ["In Transit", "Delayed"]])
    # high risk = disruptions mapping
    high_risk = len([d for d in db["disruptions"] if d["severity"] in ["HIGH", "CRITICAL"]])
    active_disruptions = len(db["disruptions"])
    
    total_cap = sum([v["capacity_kg"] for v in db["vehicles"]])
    total_load = sum([v["current_load_kg"] for v in db["vehicles"]])
    avg_util = round((total_load / total_cap * 100) if total_cap > 0 else 0)
    
    return jsonify({
        "total_vehicles": total_vehicles,
        "active_shipments": active_shipments,
        "high_risk_shipments": high_risk,
        "active_disruptions": active_disruptions,
        "average_utilization": avg_util
    })

@app.route('/api/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify(db["vehicles"])

@app.route('/api/shipments', methods=['GET'])
def get_shipments():
    return jsonify(db["shipments"])

@app.route('/api/disruptions', methods=['GET'])
def get_disruptions():
    return jsonify(db["disruptions"])

@app.route('/api/optimize-fleet', methods=['POST'])
def optimize_fleet():
    return jsonify({
        "status": "success",
        "before": {
            "average_utilization": 62,
            "high_risk_shipments": 8,
            "delayed_shipments": 18
        },
        "after": {
            "average_utilization": 81,
            "high_risk_shipments": 3,
            "delayed_shipments": 7
        },
        "reassignments": [
            {
                "shipment_id": "S102",
                "current_vehicle": "V001",
                "recommended_vehicle": "V004",
                "reason": "V004 has sufficient capacity and skirts the heavy traffic zone."
            }
        ],
        "message": "Optimization complete using local AI fallback.",
        "note": "Estimated results based on the demonstration dataset."
    })

@app.route('/api/ai/chat', methods=['POST'])
def ai_chat():
    data = request.json
    question = data.get("question", "").lower()
    
    if "risk" in question:
        return jsonify({"answer": "There are 3 high-risk shipments: S102, S115, and S121. S102 should be prioritized due to heavy traffic on the Rajkot-Ahmedabad route."})
    elif "underutilized" in question:
        return jsonify({"answer": "Vehicle V004 is currently underutilized (25% capacity). It has 900kg available capacity and is stationed in Surat."})
    else:
        return jsonify({"answer": "AI service unavailable. Using local logistics recommendation engine. I can assist with risk assessments and fleet underutilization metrics."})

@app.route('/api/ai/recommend', methods=['POST'])
def ai_recommend():
    data = request.json
    sid = data.get("shipment_id")
    if sid == "S102":
        return jsonify({
            "recommendation": "Reassign Shipment S102 to V004.",
            "reason": "V001 is nearing capacity and heading into heavy traffic. V004 is underutilized and can safely absorb the 500kg load while detouring the disruption."
        })
    return jsonify({"recommendation": "Maintain current route.", "reason": "No critical disruption thresholds crossed."})

@app.route('/api/analyze-risk', methods=['POST'])
def analyze_risk():
    data = request.json
    score = 20
    reasons = []
    if "traffic" in data.get("conditions", ""):
        score += 25
        reasons.append("Heavy traffic")
    if data.get("deadline_tight"):
        score += 20
        reasons.append("Tight delivery deadline")
        
    score = min(score + 35, 100) # Baseline fake score for demo
    
    if score < 30: level = "LOW"
    elif score < 60: level = "MEDIUM"
    elif score < 80: level = "HIGH"
    else: level = "CRITICAL"
    
    return jsonify({
        "risk_score": score,
        "risk_level": level,
        "reasons": reasons
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)

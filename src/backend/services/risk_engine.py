
def calculate_risk(conditions):
    score = 0
    reasons = []
    
    if "Heavy Traffic" in conditions:
        score += 25
        reasons.append("Heavy traffic")
    if "Rain" in conditions or "Severe Weather" in conditions:
        score += 20
        reasons.append("Severe weather")
    if "Vehicle Problem" in conditions:
        score += 30
        reasons.append("Vehicle problem")
    if "Tight Deadline" in conditions:
        score += 20
        reasons.append("Tight delivery deadline")
    if "Route Blocked" in conditions:
        score += 30
        reasons.append("Route blocked")
        
    score = min(score, 100)
    
    if score <= 30: level = "LOW"
    elif score <= 60: level = "MEDIUM"
    elif score <= 80: level = "HIGH"
    else: level = "CRITICAL"
    
    return {
        "risk_score": score,
        "risk_level": level,
        "reasons": reasons
    }

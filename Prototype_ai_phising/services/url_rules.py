import re

def evaluate_url(url: str):
    score = 0
    reasons = []

    rules = [
        {"check": lambda u: len(u) > 75, "penalty": 1, "message": "URL too long"},
        {"check": lambda u: "@" in u, "penalty": 3, "message": "Contains @"},
        {"check": lambda u: not u.startswith("https"), "penalty": 2, "message": "No HTTPS"},
        {"check": lambda u: re.search(r"\d+\.\d+\.\d+\.\d+", u), "penalty": 3, "message": "Uses IP"},
        {"check": lambda u: u.count('.') > 3, "penalty": 2, "message": "Too many subdomains"},
        {"check": lambda u: any(w in u.lower() for w in ["login","verify","bank","secure"]), "penalty": 2, "message": "Sensitive words"},
    ]

    for rule in rules:
        if rule["check"](url):
            score += rule["penalty"]
            reasons.append(rule["message"])

    if score >= 6:
        verdict = "Phishing"
    elif score >= 3:
        verdict = "Suspicious"
    else:
        verdict = "Safe"

    return {"risk_score": score, "verdict": verdict, "reasons": reasons}

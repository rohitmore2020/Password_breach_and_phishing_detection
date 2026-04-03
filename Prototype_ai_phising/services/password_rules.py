import re

def evaluate_password(password: str):
    score = 0
    issues = []

    rules = [
        {"check": lambda p: len(p) < 8, "penalty": 2, "message": "Password too short"},
        {"check": lambda p: not re.search(r"[A-Z]", p), "penalty": 1, "message": "Missing uppercase"},
        {"check": lambda p: not re.search(r"[a-z]", p), "penalty": 1, "message": "Missing lowercase"},
        {"check": lambda p: not re.search(r"\d", p), "penalty": 1, "message": "Missing number"},
        {"check": lambda p: not re.search(r"[!@#$%^&*]", p), "penalty": 1, "message": "Missing special char"},
        {"check": lambda p: "123" in p or "password" in p.lower(), "penalty": 3, "message": "Common pattern"},
    ]

    for rule in rules:
        if rule["check"](password):
            score += rule["penalty"]
            issues.append(rule["message"])

    if score <= 2:
        strength = "Strong"
    elif score <= 5:
        strength = "Medium"
    else:
        strength = "Weak"

    return {"risk_score": score, "strength": strength, "issues": issues}

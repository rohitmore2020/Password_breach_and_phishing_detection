# 🔐 Phishing Detection & Password Analyzer (FastAPI)

## 🚀 Overview

A simple rule-based cybersecurity API that:

* Checks password strength
* Detects suspicious/phishing URLs

Built using **FastAPI** for fast and lightweight performance.

---

## 🛠️ Setup

```bash
unzip ai_phishing_fastapi.zip
cd ai_phishing_fastapi

python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🌐 API Docs

Open: http://127.0.0.1:8000/docs

---

## 📌 Endpoints

### 🔐 Password Check

**POST** `/password-check`

Input:

```
password: Test123
```

---

### 🌐 URL Check

**POST** `/url-check`

Input:

```
url: http://example.com
```

---

## 🧠 How It Works

Uses simple rule-based scoring:

* Adds risk points for weak patterns
* Returns score + result + reasons

---

## 👨‍💻 Author

Rohit More

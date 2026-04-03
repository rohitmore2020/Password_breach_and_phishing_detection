from fastapi import FastAPI
from routers import password, url, combined

app = FastAPI(title="AI Phishing Detection System")

app.include_router(password.router)
app.include_router(url.router)

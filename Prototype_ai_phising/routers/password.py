from fastapi import APIRouter
from services.password_rules import evaluate_password

router = APIRouter()

@router.post("/password-check")
def password_check(password: str):
    return evaluate_password(password)

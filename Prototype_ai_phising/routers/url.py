from fastapi import APIRouter
from services.url_rules import evaluate_url

router = APIRouter()

@router.post("/url-check")
def url_check(url: str):
    return evaluate_url(url)

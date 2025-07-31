from fastapi import APIRouter, HTTPException
from services.text_service import get_all_texts

router = APIRouter(prefix="/texts")

@router.get("/")
async def get_text():
    try:
        return get_all_texts()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur serveur: {e}")

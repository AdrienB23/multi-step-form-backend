from fastapi import APIRouter, HTTPException

from services.add_ons_service import get_all_add_ons

router = APIRouter(prefix="/add-ons")

@router.get("/")
async def get_add_ons():
    try:
        return get_all_add_ons()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur serveur: {e}")

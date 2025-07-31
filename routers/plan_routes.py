from fastapi import APIRouter, HTTPException

from services.plan_service import get_all_plans

router = APIRouter(prefix="/plans")

@router.get("/")
async def get_plans():
    try:
        return get_all_plans()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur serveur: {e}")

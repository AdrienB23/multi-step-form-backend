from typing import List

from fastapi import APIRouter, HTTPException, Depends

from modules.add_ons.add_ons_di import get_addons_service
from modules.add_ons.add_ons_service import AddOnsService
from modules.plans.dtos.plan_base_dto import PlanBaseDTO

router = APIRouter(prefix="/plans", tags=["Plans"])

@router.get("/", response_model=List[PlanBaseDTO])
async def get_add_ons(service: AddOnsService = Depends(get_addons_service)):
    plans = service.get_all()
    if not plans:
        raise HTTPException(status_code=404, detail="No plans found")
    return plans

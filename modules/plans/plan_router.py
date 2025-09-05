from typing import List

from fastapi import APIRouter, HTTPException, Depends

from modules.plans.dtos.plan_base_dto import PlanBaseDTO
from modules.plans.plan_di import get_plan_service
from modules.plans.plan_service import PlanService

router = APIRouter(prefix="/plans", tags=["Plans"])

@router.get("/", response_model=List[PlanBaseDTO])
async def get_plans(service: PlanService = Depends(get_plan_service)):
    plans = service.get_all()
    if not plans:
        raise HTTPException(status_code=404, detail="No plans found")
    return plans

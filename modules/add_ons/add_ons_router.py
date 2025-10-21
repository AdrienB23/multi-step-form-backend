from typing import List

from fastapi import APIRouter, HTTPException, Depends

from modules.add_ons.add_ons_di import get_addons_service
from modules.add_ons.add_ons_service import AddOnsService
from modules.add_ons.dtos.add_ons_base_dto import AddOnsBaseDTO

router = APIRouter(prefix="/add-ons", tags=["Add-Ons"])

@router.get("/", response_model=List[AddOnsBaseDTO])
async def get_add_ons(service: AddOnsService = Depends(get_addons_service)):
    addons = service.get_all()
    if not addons:
        raise HTTPException(status_code=404, detail="No addons found")
    return addons

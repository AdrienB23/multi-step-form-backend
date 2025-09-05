from typing import Dict, Union

from fastapi import APIRouter, HTTPException, Depends

from modules.texts.text_di import get_text_service
from modules.texts.text_service import TextService

router = APIRouter(prefix="/texts", tags=["Texts"])

@router.get("", response_model=Dict[str, Union[str, list]])
async def get_texts(service: TextService = Depends(get_text_service)):
    try:
        return service.get_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/header", response_model=Dict[str, Union[str, list]])
async def get_texts_header(service: TextService = Depends(get_text_service)):
    try:
        return service.get_header()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/footer", response_model=Dict[str, Union[str, list]])
async def get_texts_footer(service: TextService = Depends(get_text_service)):
    try:
        return service.get_footer()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/info", response_model=Dict[str, Union[str, list]])
async def get_texts_info(service: TextService = Depends(get_text_service)):
    try:
        return service.get_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/plan", response_model=Dict[str, Union[str, list]])
async def get_texts_plan(service: TextService = Depends(get_text_service)):
    try:
        return service.get_plan()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/add", response_model=Dict[str, Union[str, list]])
async def get_texts_add(service: TextService = Depends(get_text_service)):
    try:
        return service.get_add()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/summary", response_model=Dict[str, Union[str, list]])
async def get_texts_summary(service: TextService = Depends(get_text_service)):
    try:
        return service.get_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/thank", response_model=Dict[str, Union[str, list]])
async def get_texts_thank(service: TextService = Depends(get_text_service)):
    try:
        return service.get_thank()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/price", response_model=Dict[str, Union[str, list]])
async def get_texts_price(service: TextService = Depends(get_text_service)):
    try:
        return service.get_price()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

@router.get("/label", response_model=Dict[str, Union[str, list]])
async def get_texts_label(service: TextService = Depends(get_text_service)):
    try:
        return service.get_label()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")

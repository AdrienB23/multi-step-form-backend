from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_session, get_uow
from modules.add_ons.add_ons_repository import AddOnsRepository
from modules.add_ons.add_ons_service import AddOnsService


def get_addons_repository(session: Session = Depends(get_session),uow = Depends(get_uow)) -> AddOnsRepository:
    return AddOnsRepository(session, uow)


def get_addons_service(repo: AddOnsRepository = Depends(get_addons_repository)) -> AddOnsService:
    return AddOnsService(repo.session)

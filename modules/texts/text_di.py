from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_session, get_uow
from modules.texts.text_repository import TextRepository
from modules.texts.text_service import TextService


def get_text_repository(session: Session = Depends(get_session),uow = Depends(get_uow)) -> TextRepository:
    return TextRepository(session, uow)


def get_text_service(repo: TextRepository = Depends(get_text_repository)) -> TextService:
    return TextService(repo.session)

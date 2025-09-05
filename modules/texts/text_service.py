import json
from sqlalchemy.orm import Session
from fastapi import HTTPException

from db.database import UnitOfWork
from modules.texts.text_repository import TextRepository


def _map_texts(texts) -> dict[str, str | list]:
    if not texts:
        raise HTTPException(status_code=404, detail="No texts found")

    result = {}
    for t in texts:
        value = t.content
        try:
            result[t.text_id] = json.loads(value)
        except (json.JSONDecodeError, TypeError):
            result[t.text_id] = value
    return result


class TextService:
    def __init__(self, session: Session) -> None:
        self.uow = UnitOfWork(session_factory=lambda: session)
        self.repo = TextRepository(session, self.uow)

    def get_all(self) -> dict[str, str | list]:
        texts = self.repo.get_all()
        return _map_texts(texts)

    def get_header(self) -> dict[str, str | list]:
        texts = self.repo.get_header()
        return _map_texts(texts)

    def get_footer(self) -> dict[str, str | list]:
        texts = self.repo.get_footer()
        return _map_texts(texts)

    def get_info(self) -> dict[str, str | list]:
        texts = self.repo.get_info()
        return _map_texts(texts)

    def get_plan(self) -> dict[str, str | list]:
        texts = self.repo.get_plan()
        return _map_texts(texts)

    def get_add(self) -> dict[str, str | list]:
        texts = self.repo.get_add()
        return _map_texts(texts)

    def get_summary(self) -> dict[str, str | list]:
        texts = self.repo.get_summary()
        return _map_texts(texts)

    def get_thank(self) -> dict[str, str | list]:
        texts = self.repo.get_thank()
        return _map_texts(texts)

    def get_price(self) -> dict[str, str | list]:
        texts = self.repo.get_price()
        return _map_texts(texts)

    def get_label(self) -> dict[str, str | list]:
        texts = self.repo.get_label()
        return _map_texts(texts)

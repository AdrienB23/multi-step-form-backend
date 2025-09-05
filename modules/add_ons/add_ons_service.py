from typing import List

from sqlalchemy.orm import Session

from db.database import UnitOfWork
from modules.add_ons.add_ons_repository import AddOnsRepository
from modules.add_ons.dtos.add_ons_base_dto import AddOnsBaseDTO


class AddOnsService:
    def __init__(self, session: Session) -> None:
        self.uow = UnitOfWork(session_factory=lambda: session)
        self.repo = AddOnsRepository(session, self.uow)

    def get_all(self) -> List[AddOnsBaseDTO]:
        result = []
        addons = self.repo.get_all()
        if not addons:
            return []
        for addon in addons:
            result.append(AddOnsBaseDTO.from_orm(addon))
        return result

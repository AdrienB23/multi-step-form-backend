from typing import List

from sqlalchemy.orm import Session

from db.database import UnitOfWork
from modules.plans.dtos.plan_base_dto import PlanBaseDTO
from modules.plans.plan_repository import PlanRepository


class PlanService:
    def __init__(self, session: Session) -> None:
        self.uow = UnitOfWork(session_factory=lambda: session)
        self.repo = PlanRepository(session, self.uow)

    def get_all(self) -> List[PlanBaseDTO]:
        result = []
        plans = self.repo.get_all()
        if not plans:
            return []
        for plan in plans:
            result.append(PlanBaseDTO.from_orm(plan))
        return result

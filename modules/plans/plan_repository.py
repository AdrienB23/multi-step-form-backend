from sqlalchemy.orm import Session

from db.database import UnitOfWork
from modules.plans.plan_model import PlanModel


class PlanRepository:
    def __init__(self, session: Session, uow: UnitOfWork):
        self.session = session
        self.uow = uow

    def get_all(self) -> list[type[PlanModel]]:
        return self.session.query(PlanModel).all()

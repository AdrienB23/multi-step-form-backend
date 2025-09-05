from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_session, get_uow
from modules.plans.plan_repository import PlanRepository
from modules.plans.plan_service import PlanService


def get_plan_repository(session: Session = Depends(get_session),uow = Depends(get_uow)) -> PlanRepository:
    return PlanRepository(session, uow)


def get_plan_service(repo: PlanRepository = Depends(get_plan_repository)) -> PlanService:
    return PlanService(repo.session)

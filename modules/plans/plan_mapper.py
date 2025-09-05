from modules.plans.dtos.plan_base_dto import PlanBaseDTO
from modules.plans.plan_model import PlanModel


class PlanMapper:

    @staticmethod
    def to_dto(entity: PlanModel) -> PlanBaseDTO:
        return PlanBaseDTO.model_validate(entity)

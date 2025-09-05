from modules.add_ons.add_ons_model import AddOnsModel
from modules.add_ons.dtos.add_ons_base_dto import AddOnsBaseDTO


class AddOnsMapper:

    @staticmethod
    def to_dto(entity: AddOnsModel) -> AddOnsBaseDTO:
        return AddOnsBaseDTO.model_validate(entity)

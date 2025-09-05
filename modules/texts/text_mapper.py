from modules.texts.dtos.text_response import TextResponse
from modules.texts.text_model import Text


class TextMapper:

    @staticmethod
    def to_dto(entity: Text) -> TextResponse:
        return TextResponse.model_validate(entity)

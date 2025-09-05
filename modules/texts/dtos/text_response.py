from modules.texts.dtos.text_base import TextBase
from pydantic import Field
from typing import Union


class TextResponse(TextBase):
    text_id: str = Field(alias="text_id")
    content: Union[str, list]

    class Config:
        from_attributes = True

from pydantic import BaseModel


class TextBase(BaseModel):
    text_id: str
    content: str

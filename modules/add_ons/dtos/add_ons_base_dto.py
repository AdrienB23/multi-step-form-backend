from pydantic import BaseModel


class AddOnsBaseDTO(BaseModel):
    add_ons_id: int
    label: str
    description: str
    price_m: int
    price_y: int

    class Config:
        from_attributes = True

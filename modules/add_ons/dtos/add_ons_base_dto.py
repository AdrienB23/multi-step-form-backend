from pydantic import BaseModel


class AddOnsBaseDTO(BaseModel):
    add_ons_id: int
    label: str
    description: str
    monthly_price: int
    yearly_price: int

    class Config:
        from_attributes = True

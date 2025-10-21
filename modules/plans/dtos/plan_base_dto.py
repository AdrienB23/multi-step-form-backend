from pydantic import BaseModel


class PlanBaseDTO(BaseModel):
    plan_id: int
    name: str
    price_m: int
    price_y: int

    class Config:
        from_attributes = True

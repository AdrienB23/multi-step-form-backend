from pydantic import BaseModel


class PlanBaseDTO(BaseModel):
    plan_id: int
    name: str
    monthly_price: int
    yearly_price: int

    class Config:
        from_attributes = True

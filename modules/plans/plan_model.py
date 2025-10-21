from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class PlanModel(Base):
    __tablename__ = "t_plan"

    plan_id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    price_m: Mapped[int] = mapped_column(Integer(), nullable=False)
    price_y: Mapped[int] = mapped_column(Integer(), nullable=False)

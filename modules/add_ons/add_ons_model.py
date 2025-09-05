from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class AddOnsModel(Base):
    __tablename__ = "t_add_ons"

    add_ons_id: Mapped[int] = mapped_column(Integer(), primary_key=True, index=True)
    label: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    monthly_price: Mapped[int] = mapped_column(Integer(), nullable=False)
    yearly_price: Mapped[int] = mapped_column(Integer(), nullable=False)

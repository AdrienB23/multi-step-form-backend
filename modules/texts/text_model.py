from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class Text(Base):
    __tablename__ = "t_text"

    text_id: Mapped[str] = mapped_column(String(50), primary_key=True, index=True)
    content: Mapped[str] = mapped_column(String(200), nullable=False)

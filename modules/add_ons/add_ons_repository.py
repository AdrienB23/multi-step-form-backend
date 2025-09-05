from sqlalchemy.orm import Session

from db.database import UnitOfWork
from modules.add_ons.add_ons_model import AddOnsModel


class AddOnsRepository:
    def __init__(self, session: Session, uow: UnitOfWork):
        self.session = session
        self.uow = uow

    def get_all(self) -> list[type[AddOnsModel]]:
        return self.session.query(AddOnsModel).all()

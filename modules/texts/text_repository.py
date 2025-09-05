from sqlalchemy.orm import Session

from db.database import UnitOfWork
from modules.texts.text_model import Text


class TextRepository:
    def __init__(self, session: Session, uow: UnitOfWork):
        self.session = session
        self.uow = uow

    def get_all(self) -> list[type[Text]]:
        return self.session.query(Text).all()

    def get_header(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("header.%")).all()

    def get_footer(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("footer.%")).all()

    def get_info(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("info.%")).all()

    def get_plan(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("plan.%")).all()

    def get_add(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("add.%")).all()

    def get_summary(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("summary.%")).all()

    def get_thank(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("thank.%")).all()

    def get_price(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("price.%")).all()

    def get_label(self) -> list[type[Text]]:
        return self.session.query(Text).filter(Text.text_id.like("label.%")).all()

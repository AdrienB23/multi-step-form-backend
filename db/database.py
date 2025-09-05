import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from db.config import DatabaseConfig
db_config = DatabaseConfig()
# Gestion des pools de connexions
engine = create_engine(
    db_config.database_connectionstring,
    echo=db_config.echo,
    future=True,
    pool_size=db_config.pool_size,  # nb max connexions simultanées
    max_overflow=db_config.max_overflow,  # connexions supplémentaires temporaires
    pool_pre_ping=db_config.pool_pre_ping,  # vérifie si connexion encore valide
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_uow():
    return UnitOfWork(SessionLocal)


class UnitOfWork:

    def __init__(self, session_factory):
        self.session_factory = session_factory

    @contextmanager
    def __call__(self):
        session = self.session_factory()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

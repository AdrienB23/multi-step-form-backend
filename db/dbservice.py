import json
from datetime import date, datetime

# import logging

from sqlmodel import Session, create_engine


def _default(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def dumps(d):
    return json.dumps(d, default=_default)


class DbService:
    engine: any

    def __init__(self, connection_string):
        try:
            self.engine = create_engine(connection_string, json_serializer=dumps)
            self.session = Session(self.engine)
        except Exception as e:
            print(f"Error while connecting to Database: {e}")
            raise e

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"close sessions {self.session.info}")
        self.session.close()

    # def getSession(self) :
    #    with DbService() as db:
    #         yield db

    # def initDb(self):
    #     # SQLModel.metadata.reflect(self.engine) # TMP Purge DB
    #     # SQLModel.metadata.drop_all(self.engine) # TMP Purge DB
    #     SQLModel.metadata.create_all(self.engine)

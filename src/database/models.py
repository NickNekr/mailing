from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from config import ConfigDB

engine = create_engine(ConfigDB.SQLALCHEMY_DATABASE_URI, echo=True)
Base = declarative_base()


class Mails(Base):
    __tablename__ = "mails"
    id = Column(Integer, primary_key=True)
    to_send = Column(String(256))
    sent = Column(Boolean, default=True)

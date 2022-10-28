from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE


class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bus = Column(String(30), nullable=True)
    station = Column(String(30), nullable=True)


class User(BaseModel):
    id   : int
    bus : str
    station  : str



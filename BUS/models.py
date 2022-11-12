from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE


class BusTable(Base):
    __tablename__ = 'bus'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    bus_name = Column(String(45), primary_key=True, nullable=True)
    bus_Id = Column(Integer)


class Bus(BaseModel):
    # id : int
    bus_name  : str
    bus_Id : int



from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE


class BusTable(Base):
    __tablename__ = 'bus'
    bus_name = Column(String(45), nullable=True)
    bus_Id = Column(Integer)


class Bus(BaseModel):
    bus_name  : str
    bus_Id : int



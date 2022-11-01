from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE


class StationTable(Base):
    __tablename__ = 'bus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    station_name = Column(String(30), nullable=True)


class Station(BaseModel):
    id   : int
    station_name  : str



from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base
from database import ENGINE

from sqlalchemy.orm import relationship




class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, aytoincrement=True)
    name = Column(String(50), nullable=False)
    timezone = Column(Integer)
    current_time = Column(Integer)


class User(BaseModel):
    id   : int
    name : str
    timeZone  : str
    current_time : int

from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base
from database import ENGINE


class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=True)
    age = Column(Integer)


class User(BaseModel):
    id   : int
    name : str
    age  : int


def main():
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()
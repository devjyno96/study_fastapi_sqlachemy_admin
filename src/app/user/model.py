from sqlalchemy import Column, Integer, String
from src.app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    test = Column(String)
    test2 = Column(String)
    test23 = Column(String)
    testes2 = Column(String)

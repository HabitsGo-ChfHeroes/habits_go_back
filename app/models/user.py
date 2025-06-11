from sqlalchemy import Column, Integer, String, Numeric, Enum
from app.enums.goal import GoalEnum
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    height = Column(Numeric(5, 2), nullable=False)
    weight = Column(Numeric(5, 2), nullable=False)
    imc = Column(Numeric(5, 2), nullable=False)
    goal = Column(Enum(GoalEnum), nullable=False)
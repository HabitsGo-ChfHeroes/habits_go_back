from sqlalchemy import Column, Integer, String, Numeric, Enum
from app.enums.goal import GoalEnum
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    height = Column(Numeric(5, 2), nullable=False)
    weight = Column(Numeric(5, 2), nullable=False)
    imc = Column(Numeric(5, 2), nullable=False)
    goal = Column(Enum(GoalEnum), nullable=False)

    plans = relationship("Plan", back_populates="user", lazy="selectin")
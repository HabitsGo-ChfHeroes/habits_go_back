from sqlalchemy import Column, Integer, Time, Enum
from app.enums.meal_type import MealTypeEnum
from sqlalchemy.orm import relationship
from app.db.base import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(MealTypeEnum), nullable=False)
    hour = Column(Time, nullable=False)

    plan_foods = relationship("PlanFood", back_populates="meal", lazy="selectin")
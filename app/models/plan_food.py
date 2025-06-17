from sqlalchemy import Column, Integer, Enum, ForeignKey
from app.enums.status import Status
from sqlalchemy.orm import relationship
from app.db.base import Base

class PlanFood(Base):
    __tablename__ = "plan_foods"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False)
    status = Column(Enum(Status), nullable=False, default = Status.NOT_COMPLETED)

    plan = relationship("Plan", back_populates="plan_foods")
    meal = relationship("Meal", back_populates="plan_foods")
    food = relationship("Food", back_populates="plan_foods")
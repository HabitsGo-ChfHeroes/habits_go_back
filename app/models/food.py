from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    preparation = Column(Text, nullable=False)
    video_url = Column(String(150), nullable=True)

    food_ingredients = relationship("FoodIngredient", back_populates="food", lazy="selectin")
    plan_foods = relationship("PlanFood", back_populates="food", lazy="selectin")
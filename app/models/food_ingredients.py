from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class FoodIngredient(Base):
    __tablename__ = "food_ingredients"

    food_id = Column(Integer, ForeignKey("foods.id"), primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True, nullable=False)

    food = relationship("Food", back_populates="food_ingredients")
    ingredient = relationship("Ingredient", back_populates="food_ingredients")
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    quantity = Column(Numeric(5, 2), nullable=False)
    unit = Column(String(100), nullable=True)

    food_ingredients = relationship("FoodIngredient", back_populates="food", lazy="selectin")
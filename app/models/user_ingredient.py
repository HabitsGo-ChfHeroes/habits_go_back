from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class UserIngredient(Base):
    __tablename__ = "user_ingredients"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), primary_key=True, nullable=False)

    user = relationship("User", back_populates="user_ingredients")
    ingredient = relationship("Ingredient", back_populates="user_ingredients")
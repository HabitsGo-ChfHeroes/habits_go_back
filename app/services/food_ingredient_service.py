from sqlalchemy.orm import Session
from app.schemas.food_ingredient_schema import FoodIngredientCreate, FoodIngredientResponse
from app.repositories.food_ingredient_repository import create_food_ingredient, create_food_ingredient_uncommitted

def create_food_ingredient_entry(db: Session, data: FoodIngredientCreate) -> FoodIngredientResponse:
    food_ingredient = create_food_ingredient(db, data)
    return FoodIngredientResponse.model_validate(food_ingredient)

def create_food_ingredient_entry_uncommitted(db: Session, data: FoodIngredientCreate):
    return create_food_ingredient_uncommitted(db, data)
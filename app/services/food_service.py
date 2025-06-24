from sqlalchemy.orm import Session
from app.schemas.food_schema import FoodCreate, FoodResponse
from app.repositories.food_repository import create_food, create_food_uncommitted

def create_food_entry(db: Session, data: FoodCreate) -> FoodResponse:
    food = create_food(db, data)
    return FoodResponse.model_validate(food)


def create_food_entry_uncommitted(db: Session, data: FoodCreate):
    return create_food_uncommitted(db, data)
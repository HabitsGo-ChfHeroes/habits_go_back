from sqlalchemy.orm import Session
from app.schemas.food_schema import FoodCreate, FoodResponse
from app.repositories.food_repository import create_food

def create_food_entry(db: Session, data: FoodCreate) -> FoodResponse:
    return create_food(db, data)
from sqlalchemy.orm import Session
from app.schemas.meal_schema import MealCreate, MealResponse
from app.repositories.meal_repository import create_meal, create_meal_uncommitted

def create_meal_entry(db: Session, data: MealCreate) -> MealResponse:
    meal = create_meal(db, data)
    return MealResponse.model_validate(meal)

def create_meal_entry_uncommitted(db: Session, data: MealCreate):
    return create_meal_uncommitted(db, data)
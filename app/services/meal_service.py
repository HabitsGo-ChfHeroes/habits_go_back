from sqlalchemy.orm import Session
from app.schemas.meal_schema import MealCreate, MealResponse
from app.repositories.meal_repository import create_meal

def create_meal_entry(db: Session, data: MealCreate) -> MealResponse:
    meal = create_meal(db, data)
    return MealResponse.model_validate(meal)

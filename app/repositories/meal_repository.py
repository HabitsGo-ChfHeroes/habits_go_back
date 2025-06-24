from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.schemas.meal_schema import MealCreate

def create_meal(db: Session, meal_data: MealCreate) -> Meal:
    new_meal = Meal(
        name=meal_data.name,
        hour=meal_data.hour
    )
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

def create_meal_uncommitted(db: Session, data: MealCreate) -> Meal:
    new_meal = Meal(
        name=data.name,
        hour=data.hour
    )
    db.add(new_meal)
    db.flush()
    return new_meal

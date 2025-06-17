from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.schemas.meal_schema import MealCreate, MealResponse

def create_meal(db: Session, meal_data: MealCreate) -> MealResponse:
    new_meal = Meal(
        name = meal_data.name,
        hour = meal_data.hour
    )
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)

    return MealResponse.model_validate(new_meal)

from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.meal import Meal
from app.schemas.meal_schema import MealCreate, MealResponse

def create_meal(meal_data: MealCreate) -> MealResponse:
    db: Session = next(get_session())
    new_meal = Meal(
        name = meal_data.name,
        hour = meal_data.hour
    )
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)

    return MealResponse.model_validate(new_meal)

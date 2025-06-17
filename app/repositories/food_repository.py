from sqlalchemy.orm import Session
from app.models.food import Food
from app.schemas.food_schema import FoodCreate, FoodResponse

def create_food(db: Session, food_data: FoodCreate) -> FoodResponse:
    new_food = Food(
        name = food_data.name,
        preparation = food_data.preparation,
        video_url = food_data.video_url
    )
    db.add(new_food)
    db.commit()
    db.refresh(new_food)

    return FoodResponse.model_validate(new_food)

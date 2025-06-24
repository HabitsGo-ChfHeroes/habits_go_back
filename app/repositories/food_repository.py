from sqlalchemy.orm import Session
from app.models.food import Food
from app.schemas.food_schema import FoodCreate

def create_food(db: Session, food_data: FoodCreate) -> Food:
    new_food = Food(
        name=food_data.name,
        preparation=food_data.preparation,
        video_url=food_data.video_url
    )
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food

def create_food_uncommitted(db: Session, data: FoodCreate) -> Food:
    new_food = Food(
        name=data.name,
        preparation=data.preparation,
        video_url=data.video_url
    )
    db.add(new_food)
    db.flush()
    return new_food

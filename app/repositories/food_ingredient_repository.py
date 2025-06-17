from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.food_ingredient import FoodIngredient
from app.schemas.food_ingredient_schema import FoodIngredientCreate, FoodIngredientResponse

def create_food_ingredient(food_ingredient_data: FoodIngredientCreate) -> FoodIngredientResponse:
    db: Session = next(get_session())
    new_link = FoodIngredient(
        food_id=food_ingredient_data.food_id,
        ingredient_id=food_ingredient_data.ingredient_id
    )

    db.add(new_link)
    db.commit()
    db.refresh(new_link)

    return FoodIngredientResponse.model_validate(new_link)

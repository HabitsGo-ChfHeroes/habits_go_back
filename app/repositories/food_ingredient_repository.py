from sqlalchemy.orm import Session
from app.models.food_ingredient import FoodIngredient
from app.schemas.food_ingredient_schema import FoodIngredientCreate, FoodIngredientResponse

def create_food_ingredient(db: Session, food_ingredient_data: FoodIngredientCreate) -> FoodIngredientResponse:
    new_food_ingredient = FoodIngredient(
        food_id=food_ingredient_data.food_id,
        ingredient_id=food_ingredient_data.ingredient_id
    )
    db.add(new_food_ingredient)
    db.commit()
    db.refresh(new_food_ingredient)

    return FoodIngredientResponse.model_validate(new_food_ingredient)

from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient
from app.schemas.ingredient_schema import IngredientCreate, IngredientResponse

def create_ingredient(db: Session, ingredient_data: IngredientCreate) -> IngredientResponse:
    new_ingredient = Ingredient(
        name = ingredient_data.name,
        quantity = ingredient_data.quantity,
        unit = ingredient_data.unit
    )
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)

    return IngredientResponse.model_validate(new_ingredient)

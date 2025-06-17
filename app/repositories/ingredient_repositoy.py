from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.ingredient import Ingredient
from app.schemas.ingredient_schema import IngredientCreate, IngredientResponse

def create_ingredient(ingredient_data: IngredientCreate) -> IngredientResponse:
    db: Session = next(get_session())
    new_ingredient = Ingredient(
        name = ingredient_data.name,
        quantity = ingredient_data.quantity,
        unit = ingredient_data.unit
    )
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)

    return IngredientResponse.model_validate(new_ingredient)

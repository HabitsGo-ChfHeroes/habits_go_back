from sqlalchemy.orm import Session
from app.schemas.ingredient_schema import IngredientCreate, IngredientResponse
from app.repositories.ingredient_repository import create_ingredient

def create_ingredient_entry(db: Session, data: IngredientCreate) -> IngredientResponse:
    ingredient = create_ingredient(db, data)
    return IngredientResponse.model_validate(ingredient)

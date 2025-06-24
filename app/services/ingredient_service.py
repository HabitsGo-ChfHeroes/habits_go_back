from sqlalchemy.orm import Session
from app.schemas.ingredient_schema import IngredientCreate, IngredientResponse
from app.repositories.ingredient_repository import create_ingredient, create_ingredient_uncommitted

def create_ingredient_entry(db: Session, data: IngredientCreate) -> IngredientResponse:
    ingredient = create_ingredient(db, data)
    return IngredientResponse.model_validate(ingredient)

def create_ingredient_entry_uncommitted(db: Session, data: IngredientCreate):
    return create_ingredient_uncommitted(db, data)
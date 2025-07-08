from sqlalchemy.orm import Session
from app.schemas.ingredient_schema import IngredientCreate, IngredientResponse
from app.repositories.ingredient_repository import create_ingredient, create_ingredient_uncommitted, get_ingredients_paginated, search_ingredients_by_name

def create_ingredient_entry(db: Session, data: IngredientCreate) -> IngredientResponse:
    ingredient = create_ingredient(db, data)
    return IngredientResponse.model_validate(ingredient)

def create_ingredient_entry_uncommitted(db: Session, data: IngredientCreate):
    return create_ingredient_uncommitted(db, data)

def fetch_paginated_ingredients(db: Session, skip: int = 0, limit: int = 50) -> list[dict]:
    return get_ingredients_paginated(db, skip, limit)

def search_ingredient_id_name_by_term(db: Session, query: str) -> list[dict]:
    return search_ingredients_by_name(db, query)
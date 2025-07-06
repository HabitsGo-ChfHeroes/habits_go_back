from sqlalchemy.orm import Session
from app.schemas.user_ingredient_schema import UserIngredientCreate, UserIngredientResponse
from app.schemas.ingredient_schema import IngredientResponse
from app.repositories.user_ingredient_repository import create_user_ingredient, create_user_ingredient_uncommitted, get_ingredients_by_user_id, delete_user_ingredient

def create_user_ingredient_entry(db: Session, data: UserIngredientCreate) -> UserIngredientResponse:
    user_ingredient = create_user_ingredient(db, data)
    return UserIngredientResponse.model_validate(user_ingredient)

def create_user_ingredient_entry_uncommitted(db: Session, data: UserIngredientCreate):
    return create_user_ingredient_uncommitted(db, data)

def get_user_ingredients(db: Session, user_id: int) -> list[IngredientResponse]:
    ingredients = get_ingredients_by_user_id(db, user_id)
    return [IngredientResponse.model_validate(ing) for ing in ingredients]

def remove_user_ingredient_entry(db: Session, user_id: int, ingredient_id: int) -> bool:
    return delete_user_ingredient(db, user_id, ingredient_id)
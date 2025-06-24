from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient
from app.schemas.ingredient_schema import IngredientCreate

def create_ingredient(db: Session, ingredient_data: IngredientCreate) -> Ingredient:
    new_ingredient = Ingredient(
        name=ingredient_data.name,
        quantity=ingredient_data.quantity,
        unit=ingredient_data.unit
    )
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient

def create_ingredient_uncommitted(db: Session, data: IngredientCreate) -> Ingredient:
    new_ingredient = Ingredient(
        name=data.name,
        quantity=data.quantity,
        unit=data.unit
    )
    db.add(new_ingredient)
    db.flush()
    return new_ingredient

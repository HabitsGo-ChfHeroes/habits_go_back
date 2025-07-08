from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient
from app.schemas.ingredient_schema import IngredientCreate
from sqlalchemy import func

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

def get_ingredients_paginated(db: Session, skip: int = 0, limit: int = 50) -> list[dict]:
    result = db.query(Ingredient.id, Ingredient.name).offset(skip).limit(limit).all()
    return [{"id": row.id, "name": row.name} for row in result]

def search_ingredients_by_name(db: Session, query: str) -> list[dict]:
    result = (
        db.query(func.min(Ingredient.id).label("id"), Ingredient.name)
        .filter(Ingredient.name.ilike(f"%{query}%"))
        .group_by(Ingredient.name)
        .order_by(func.min(Ingredient.id))
        .all()
    )
    return [{"id": row.id, "name": row.name} for row in result]

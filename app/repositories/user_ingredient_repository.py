from sqlalchemy.orm import Session
from app.models.user_ingredient import UserIngredient
from app.models.ingredient import Ingredient
from app.schemas.user_ingredient_schema import UserIngredientCreate

def create_user_ingredient(db: Session, user_ingredient_data: UserIngredientCreate) -> UserIngredient:
    new_user_ingredient = UserIngredient(
        user_id=user_ingredient_data.user_id,
        ingredient_id=user_ingredient_data.ingredient_id
    )
    db.add(new_user_ingredient)
    db.commit()
    db.refresh(new_user_ingredient)

    return new_user_ingredient

def create_user_ingredient_uncommitted(db: Session, data: UserIngredientCreate):
    new_user_ingredient = UserIngredient(
        user_id=data.user_id,
        ingredient_id=data.ingredient_id
    )
    db.add(new_user_ingredient)
    return new_user_ingredient

def get_ingredients_by_user_id(db: Session, user_id: int) -> list[Ingredient]:
    return (
        db.query(Ingredient)
        .join(UserIngredient, Ingredient.id == UserIngredient.ingredient_id)
        .filter(UserIngredient.user_id == user_id)
        .all()
    )
    
def delete_user_ingredient(db: Session, user_id: int, ingredient_id: int) -> bool:
    relation = db.query(UserIngredient).filter_by(user_id=user_id, ingredient_id=ingredient_id).first()
    if relation:
        db.delete(relation)
        db.commit()
        return True
    return False

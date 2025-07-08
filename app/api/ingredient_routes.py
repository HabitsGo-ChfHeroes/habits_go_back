from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.schemas.ingredient_schema import IngredientCreate, IngredientResponse
from app.services.ingredient_service import create_ingredient_entry, fetch_paginated_ingredients, search_ingredient_id_name_by_term

router = APIRouter()

@router.post("/", response_model=IngredientResponse)
def create_ingredient(data: IngredientCreate, db: Session = Depends(get_session)):
    return create_ingredient_entry(db, data)

@router.get("/list", response_model=list[dict])
def get_ingredient_id_name_list(skip: int = 0, limit: int = 50, db: Session = Depends(get_session)):
    return fetch_paginated_ingredients(db, skip, limit)

@router.get("/search", response_model=list[dict])
def search_ingredients(query: str, db: Session = Depends(get_session)):
    return search_ingredient_id_name_by_term(db, query)
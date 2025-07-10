from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserResponse, UserUpdate
from app.schemas.ingredient_schema import IngredientResponse
from app.schemas.user_ingredient_schema import UserIngredientCreate, UserIngredientResponse
from app.schemas.user_habit_schema import UserHabitCreate, UserHabitResponse
from app.services.user_service import (
    get_user_details_by_id,
    get_weekly_completion,
    get_most_productive_day,
    get_meals_completion_summary_string,
    get_weekly_evolution_data,
    update_user_profile,
)
from app.services.user_habit_service import submit_user_habits
from app.services.user_ingredient_service import create_user_ingredient_entry, get_user_ingredients, remove_user_ingredient_entry

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_session)):
    user = get_user_details_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/weekly/completion", response_model=int)
def get_weekly_completion_endpoint(
    user_id: int,
    weekOffset: int = 0,
    db: Session = Depends(get_session),
):
    return get_weekly_completion(user_id, db, weekOffset)

@router.get("/{user_id}/weekly/top/days", response_model=str)
def get_most_productive_day_endpoint(
    user_id: int,
    weekOffset: int = 0,
    db: Session = Depends(get_session),
):
    return get_most_productive_day(db, user_id, weekOffset)

@router.get("/{user_id}/meal/completion/summary", response_model=str)
def get_meals_completion_summary(
    user_id: int,
    weekOffset: int = 0,
    db: Session = Depends(get_session),
):
    return get_meals_completion_summary_string(db, user_id, weekOffset)

@router.get("/{user_id}/weekly/evolution", response_model=list[int])
def get_weekly_evolution_per_day(
    user_id: int,
    weekOffset: int = 0,
    db: Session = Depends(get_session),
):
    return get_weekly_evolution_data(db, user_id, weekOffset)

@router.put("/{user_id}/profile", response_model=UserResponse)
def update_user(user_id: int, update_data: UserUpdate, db: Session = Depends(get_session)):
    return update_user_profile(db, user_id, update_data)

@router.post("/{user_id}/habits", response_model=UserHabitResponse)
def submit_habits(
    user_id: int,
    habit_data: UserHabitCreate,
    db: Session = Depends(get_session),
):
    return submit_user_habits(db, user_id, habit_data)

@router.post("/{user_id}/ingredients/{ingredient_id}", response_model=UserIngredientResponse, status_code=status.HTTP_201_CREATED)
def create_user_ingredient(user_id: int, ingredient_id: int, db: Session = Depends(get_session)):
    payload = UserIngredientCreate(user_id=user_id, ingredient_id=ingredient_id)
    try:
        rel = create_user_ingredient_entry(db, payload)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid user_id or ingredient_id, or relationship already exists"
        )
    return rel

@router.get("/{user_id}/favorite-ingredients", response_model=list[IngredientResponse])
def list_user_ingredients(user_id: int, db: Session = Depends(get_session)):
    return get_user_ingredients(db, user_id)

@router.delete("/{user_id}/ingredients/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_ingredient(user_id: int, ingredient_id: int, db: Session = Depends(get_session)):
    deleted = remove_user_ingredient_entry(db, user_id, ingredient_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User-ingredient relationship not found"
        )
    return

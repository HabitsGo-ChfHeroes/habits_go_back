from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserResponse, UserUpdate
from app.services.user_service import get_user_details_by_id, get_weekly_completion, get_most_productive_day, get_meals_completion_summary_string, get_weekly_evolution_data, update_user_profile

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_session)):
    user = get_user_details_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/weekly/completion", response_model=int)
def get_weekly_completion_endpoint(user_id: int, db: Session = Depends(get_session)):
    return get_weekly_completion(user_id, db)

@router.get("/{user_id}/weekly/top/days", response_model=str)
def get_most_productive_day_endpoint(user_id: int, db: Session = Depends(get_session)):
    return get_most_productive_day(db, user_id)

@router.get("/{user_id}/meal/completion/summary", response_model=str)
def get_meals_completion_summary(user_id: int, db: Session = Depends(get_session)):
    return get_meals_completion_summary_string(db, user_id)

@router.get("/{user_id}/weekly/evolution", response_model=list[int])
def get_weekly_evolution_per_day(user_id: int, db: Session = Depends(get_session)):
    return get_weekly_evolution_data(db, user_id)

@router.put("/{user_id}/profile", response_model=UserResponse)
def update_user(user_id: int, update_data: UserUpdate, db: Session = Depends(get_session)):
    return update_user_profile(db, user_id, update_data)
from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.schemas.user_schema import UserResponse
from app.repositories.user_repository import get_user_by_id, get_weekly_completion_percentage
from fastapi import HTTPException

def get_user_details_by_id(db: Session, user_id: int) -> UserResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse.model_validate(user)

def get_weekly_completion(user_id: int, db: Session) -> int:
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    completed, total = get_weekly_completion_percentage(db, user_id, start_of_week, end_of_week)

    if total == 0:
        return 0
    return int((completed / total) * 100)

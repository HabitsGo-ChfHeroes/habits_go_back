from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserResponse
from app.services.user_service import get_user_details_by_id, get_weekly_completion, get_most_productive_day

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_session)):
    user = get_user_details_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/weekly/completion/{user_id}", response_model=int)
def get_weekly_completion_endpoint(user_id: int, db: Session = Depends(get_session)):
    return get_weekly_completion(user_id, db)

@router.get("/user/productive/day/{user_id}", response_model=str)
def get_most_productive_day_endpoint(user_id: int, db: Session = Depends(get_session)):
    return get_most_productive_day(db, user_id)
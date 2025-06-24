from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserResponse
from app.services.user_service import get_user_details_by_id

router = APIRouter()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_session)):
    user = get_user_details_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
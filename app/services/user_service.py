from sqlalchemy.orm import Session
from app.schemas.user_schema import UserResponse
from app.repositories.user_repository import get_user_by_id
from fastapi import HTTPException

def get_user_details_by_id(db: Session, user_id: int) -> UserResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse.model_validate(user)

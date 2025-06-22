from sqlalchemy.orm import Session
from app.schemas.user_schema import UserRequest, UserResponse
from app.repositories.user_repository import get_user_by_id
from fastapi import HTTPException

def get_user_details_by_id(db: Session, user_id: int) -> UserResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        height=user.height,
        weight=user.weight,
        goal=user.goal,
        imc=user.imc
    )
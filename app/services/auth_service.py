from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin
from app.repositories.user_repository import create_user, get_user_by_email
from app.services.user_service import calculate_imc
from fastapi import HTTPException

def register_user(db: Session, user_data: UserCreate):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    imc = calculate_imc(user_data.height, user_data.weight)
    return create_user(db, user_data, imc)

def login_user(db: Session, user_data: UserLogin):
    user = get_user_by_email(db, user_data.email)
    if user and user.password == user_data.password:
        return user
    raise HTTPException(status_code=401, detail="Invalid credentials")
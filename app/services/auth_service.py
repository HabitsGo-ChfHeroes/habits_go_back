from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin
from app.repositories.user_repository import create_user, get_user_by_email
from fastapi import HTTPException

def calculate_imc(height: float, weight: float) -> float | None:
    if not height or not weight:
        return None
    try:
        return round(weight / ((height / 100) ** 2), 2)
    except ZeroDivisionError:
        return None

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
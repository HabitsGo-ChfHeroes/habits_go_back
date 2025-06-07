from app.schemas.user_schema import UserCreate, UserLogin
from app.repositories.user_repository import create_user, get_user_by_username, get_user_by_email
from fastapi import HTTPException

def register_user(user_data: UserCreate):
    existing_user = get_user_by_username(user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(user_data)

def login_user(user_data: UserLogin):
    user = get_user_by_email(user_data.email)
    if user and user.password == user_data.password:
        return user
    raise HTTPException(status_code=401, detail="Invalid credentials")
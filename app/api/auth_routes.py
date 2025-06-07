from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserLogin, UserOut
from app.services.auth_service import register_user, login_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    return register_user(user)

@router.post("/login", response_model=UserOut)
def login(user: UserLogin):
    result = login_user(user)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result
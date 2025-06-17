from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserLogin, UserOut
from app.services.auth_service import register_user, login_user

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_session)):
    return register_user(db, user)

@router.post("/login", response_model=UserOut)
def login(user: UserLogin, db: Session = Depends(get_session)):
    result = login_user(db, user)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result
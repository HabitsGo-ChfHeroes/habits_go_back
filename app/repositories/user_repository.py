from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.user import User
from app.schemas.user_schema import UserCreate

def create_user(user_data: UserCreate):
    db: Session = next(get_session())
    new_user = User(email=user_data.email, username=user_data.username, password=user_data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(username: str):
    db: Session = next(get_session())
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(email: str):
    db: Session = next(get_session())
    return db.query(User).filter(User.email == email).first()
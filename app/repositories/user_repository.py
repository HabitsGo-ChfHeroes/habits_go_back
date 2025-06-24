from sqlalchemy.orm import Session
from sqlalchemy import func, case
from datetime import date
from typing import List
from app.models.user import User
from app.models.plan import Plan
from app.models.plan_food import PlanFood
from app.schemas.user_schema import UserCreate

def create_user(db: Session, user_data: UserCreate, imc: float | None) -> User:
    new_user = User(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        password=user_data.password,
        height=user_data.height,
        weight=user_data.weight,
        goal=user_data.goal,
        imc=imc
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_weekly_completion_percentage(db: Session, user_id: int, start_date, end_date):
    result = db.query(
        func.count(PlanFood.id).label("total"),
        func.sum(
            case((PlanFood.status == "Completado", 1), else_=0)
        ).label("completed")
    ).join(Plan, Plan.id == PlanFood.plan_id
    ).filter(
        Plan.user_id == user_id,
        Plan.date >= start_date,
        Plan.date <= end_date
    ).one()

    return result.completed or 0, result.total or 0

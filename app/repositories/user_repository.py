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

def get_most_productive_days(db: Session, user_id: int, start_date: date, end_date: date) -> List[int]:
    subquery = (
        db.query(
            func.dayofweek(Plan.date).label("weekday"),
            func.count(PlanFood.id).label("completed_count")
        )
        .join(PlanFood, Plan.id == PlanFood.plan_id)
        .filter(
            Plan.user_id == user_id,
            Plan.date >= start_date,
            Plan.date <= end_date,
            PlanFood.status == "Completado"
        )
        .group_by("weekday")
        .subquery()
    )

    max_count_subquery = db.query(func.max(subquery.c.completed_count)).scalar_subquery()

    result = (
        db.query(subquery.c.weekday)
        .filter(subquery.c.completed_count == max_count_subquery)
        .all()
    )

    return [int(row[0]) for row in result]

def get_meals_completion_counts(db: Session, user_id: int) -> tuple[int, int]:
    total_comidas_cumplidas = (
        db.query(PlanFood)
        .join(Plan)
        .filter(Plan.user_id == user_id, PlanFood.status == "Completado")
        .count()
    )

    total_comidas_registradas = (
        db.query(PlanFood)
        .join(Plan)
        .filter(Plan.user_id == user_id)
        .count()
    )

    return total_comidas_cumplidas, total_comidas_registradas

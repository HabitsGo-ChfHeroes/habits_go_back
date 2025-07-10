from sqlalchemy.orm import Session
from datetime import date, timedelta
from typing import List
from app.schemas.user_schema import UserResponse, UserUpdate
from app.repositories.user_repository import (
    get_user_by_id,
    get_weekly_completion_percentage,
    get_most_productive_days,
    get_meals_completion_counts,
    get_weekly_completed_per_day,
    save_user,
)
from fastapi import HTTPException

def calculate_imc(height: float, weight: float) -> float | None:
    if not height or not weight:
        return None
    try:
        return round(weight / ((height / 100) ** 2), 2)
    except ZeroDivisionError:
        return None

def get_user_details_by_id(db: Session, user_id: int) -> UserResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse.model_validate(user)

def get_weekly_completion(user_id: int, db: Session, week_offset: int = 0) -> int:
    """Return the completion percentage for the requested week."""

    today = date.today() - timedelta(weeks=week_offset)
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    completed, total = get_weekly_completion_percentage(
        db, user_id, start_of_week, end_of_week
    )

    if total == 0:
        return 0
    return int((completed / total) * 100)

def get_most_productive_day(db: Session, user_id: int, week_offset: int = 0) -> str:
    today = date.today() - timedelta(weeks=week_offset)
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    productive_days = get_most_productive_days(db, user_id, start_of_week, end_of_week)

    if not productive_days:
        return "NINGUNO"

    weekday_names = {
        1: "DOM", 2: "LUN", 3: "MAR", 4: "MIÉ", 5: "JUE", 6: "VIE", 7: "SÁB"
    }

    day_abbrs = [weekday_names.get(day, "") for day in productive_days]

    if len(day_abbrs) == 7:
        return "TODOS"
    elif len(day_abbrs) == 1:
        full_names = {
            "LUN": "LUNES", "MAR": "MARTES", "MIÉ": "MIÉRCOLES",
            "JUE": "JUEVES", "VIE": "VIERNES", "SÁB": "SÁBADO", "DOM": "DOMINGO"
        }
        return full_names[day_abbrs[0]]
    else:
        return ", ".join(day_abbrs)
    
def get_meals_completion_summary_string(
    db: Session, user_id: int, week_offset: int = 0
) -> str:
    today = date.today() - timedelta(weeks=week_offset)
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    completed, total = get_meals_completion_counts(
        db, user_id, start_of_week, end_of_week
    )
    return f"{completed} / {total}"

def get_weekly_evolution_data(db: Session, user_id: int, week_offset: int = 0) -> List[int]:
    today = date.today() - timedelta(weeks=week_offset)
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)

    result_map = get_weekly_completed_per_day(db, user_id, monday, sunday)

    return [
        result_map.get(monday + timedelta(days=i), 0)
        for i in range(7)
    ]

def update_user_profile(db: Session, user_id: int, update_data: UserUpdate) -> UserResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.height = update_data.height
    user.weight = update_data.weight
    user.goal = update_data.goal
    user.imc = calculate_imc(update_data.height, update_data.weight)

    updated_user = save_user(db, user)

    return UserResponse.model_validate(updated_user)

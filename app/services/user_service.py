from sqlalchemy.orm import Session
from datetime import date, timedelta
from typing import List
from app.schemas.user_schema import UserResponse
from app.repositories.user_repository import get_user_by_id, get_weekly_completion_percentage, get_most_productive_days, get_meals_completion_counts, get_weekly_completed_per_day
from fastapi import HTTPException

def get_user_details_by_id(db: Session, user_id: int) -> UserResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse.model_validate(user)

def get_weekly_completion(user_id: int, db: Session) -> int:
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    completed, total = get_weekly_completion_percentage(db, user_id, start_of_week, end_of_week)

    if total == 0:
        return 0
    return int((completed / total) * 100)

def get_most_productive_day(db: Session, user_id: int) -> str:
    today = date.today()
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
    
def get_meals_completion_summary_string(db: Session, user_id: int) -> str:
    completed, total = get_meals_completion_counts(db, user_id)
    return f"{completed} / {total}"

def get_weekly_evolution_data(db: Session, user_id: int) -> List[int]:
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)

    result_map = get_weekly_completed_per_day(db, user_id, monday, sunday)

    return [
        result_map.get(monday + timedelta(days=i), 0)
        for i in range(7)
    ]
from sqlalchemy.orm import Session
from datetime import date
from fastapi import HTTPException
from app.schemas.user_habit_schema import UserHabitCreate, UserHabitResponse
from app.repositories.user_repository import get_user_by_id
from app.repositories.user_habit_repository import (
    get_habits_by_user_id,
    create_user_habits,
    save_user_habits,
)


def submit_user_habits(db: Session, user_id: int, data: UserHabitCreate) -> UserHabitResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    habits = get_habits_by_user_id(db, user_id)
    if habits:
        habits.exercise_days = data.exercise_days
        habits.smokes = data.smokes
        habits.water_glasses = data.water_glasses
        habits.sleep_7h = data.sleep_7h
        habits.updated_at = date.today()
        habits = save_user_habits(db, habits)
    else:
        habits = create_user_habits(db, user_id, data)

    return UserHabitResponse.model_validate(habits)

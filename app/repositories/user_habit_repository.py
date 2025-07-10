from sqlalchemy.orm import Session
from datetime import date
from app.models.user_habit import UserHabit
from app.schemas.user_habit_schema import UserHabitCreate


def get_habits_by_user_id(db: Session, user_id: int) -> UserHabit | None:
    return db.query(UserHabit).filter(UserHabit.user_id == user_id).first()


def create_user_habits(db: Session, user_id: int, data: UserHabitCreate) -> UserHabit:
    new_habits = UserHabit(
        user_id=user_id,
        exercise_days=data.exercise_days,
        smokes=data.smokes,
        water_glasses=data.water_glasses,
        sleep_7h=data.sleep_7h,
        updated_at=date.today(),
    )
    db.add(new_habits)
    db.commit()
    db.refresh(new_habits)
    return new_habits


def save_user_habits(db: Session, habits: UserHabit) -> UserHabit:
    db.add(habits)
    db.commit()
    db.refresh(habits)
    return habits

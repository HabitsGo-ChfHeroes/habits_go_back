from pydantic import BaseModel
from datetime import date

class UserHabitCreate(BaseModel):
    exercise_days: int
    smokes: bool
    water_glasses: int
    sleep_7h: bool

class UserHabitResponse(BaseModel):
    user_id: int
    exercise_days: int
    smokes: bool
    water_glasses: int
    sleep_7h: bool
    updated_at: date

    model_config = {
        "from_attributes": True
    }

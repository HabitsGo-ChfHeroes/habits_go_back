from pydantic import BaseModel
from app.enums.status import Status

class DailyPlanRequest(BaseModel):
    user_id: int

class DailyPlanResponse(BaseModel):
    message: str

class PlanFoodCreate(BaseModel):
    plan_id: int
    meal_id: int
    food_id: int
    status: Status

class PlanFoodResponse(BaseModel):
    id: int
    plan_id: int
    meal_id: int
    food_id: int
    status: Status

    model_config = {
        "from_attributes": True
    }

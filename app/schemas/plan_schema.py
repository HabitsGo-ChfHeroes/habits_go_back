from pydantic import BaseModel
from datetime import date, time
from typing import List
from app.enums.status import Status

class PlanCreate(BaseModel):
    user_id: int
    date: date
    comment: str

class PlanResponse(BaseModel):
    id: int
    user_id: int
    date: date
    comment: str

    model_config = {
        "from_attributes": True
    }

class PlanMealIngredient(BaseModel):
    name: str
    quantity: float
    unit: str

class PlanMealFood(BaseModel):
    name: str
    preparation: str
    video_url: str
    ingredients: List[PlanMealIngredient]

class PlanMeal(BaseModel):
    plan_food_id: int
    name: str
    hour: time
    food: PlanMealFood
    status: Status

class PlanDetailResponse(BaseModel):
    id: int
    date: date
    comment: str
    meals: List[PlanMeal]

class PlanUpdate(BaseModel):
    comment: str
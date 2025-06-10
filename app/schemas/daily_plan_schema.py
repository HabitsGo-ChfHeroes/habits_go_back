# app/schemas/daily_plan_schema.py

from pydantic import BaseModel
from typing import List

class DailyPlanRequest(BaseModel):
    goal: str  # Ej: "Ganar masa muscular"

class Meal(BaseModel):
    type: str
    dishName: str
    ingredients: str
    preparation: str
    videoUrl: str

class DailyPlanResponse(BaseModel):
    meals: List[Meal]

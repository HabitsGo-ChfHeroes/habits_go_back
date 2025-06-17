from pydantic import BaseModel
from typing import List, Optional

class PlanFoodsRequest(BaseModel):
    goal: str

class Ingredient(BaseModel):
    name: str
    quantity: Optional[float] = None
    unit: str

class FoodDetails(BaseModel):
    name: str
    meal_type: str
    time: str
    preparation: str
    video_url: str

class Meal(BaseModel):
    food: FoodDetails
    ingredients: List[Ingredient]

class PlanFoodsResponse(BaseModel):
    meals: List[Meal]

"""
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
"""
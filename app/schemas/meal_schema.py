from pydantic import BaseModel
from datetime import time
from app.enums.meal_type import MealTypeEnum

class MealCreate(BaseModel):
    name: MealTypeEnum
    hour: time

class MealResponse(BaseModel):
    id: int
    name: MealTypeEnum
    hour: time

    model_config = {
        "from_attributes": True
    }
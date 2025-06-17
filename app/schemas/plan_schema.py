from pydantic import BaseModel
from datetime import date

class PlanCreate(BaseModel):
    user_id: int
    date: date

class PlanResponse(BaseModel):
    id: int
    user_id: int
    date: date

    model_config = {
        "from_attributes": True
    }
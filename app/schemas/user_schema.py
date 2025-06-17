from pydantic import BaseModel
from app.enums.goal import GoalEnum

class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    height: float
    weight: float
    goal: GoalEnum

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    model_config = {
        "from_attributes": True
    }
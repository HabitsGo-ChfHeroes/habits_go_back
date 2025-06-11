from pydantic import BaseModel, condecimal
from app.enums.goal import GoalEnum

Decimal5_2 = condecimal(max_digits=5, decimal_places=2)

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
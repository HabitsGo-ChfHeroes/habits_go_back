from pydantic import BaseModel
from app.enums.goal import GoalEnum

class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
    height: float
    weight: float
    goal: GoalEnum

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    goal: GoalEnum

    model_config = {
        "from_attributes": True
    }

class UserRequest(BaseModel):
    id: int

class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    height: float
    weight: float
    goal: GoalEnum
    imc: float

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    height: float
    weight: float
    goal: GoalEnum

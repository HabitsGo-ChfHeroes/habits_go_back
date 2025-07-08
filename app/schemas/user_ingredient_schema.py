from pydantic import BaseModel

class UserIngredientCreate(BaseModel):
    user_id: int
    ingredient_id: int

class UserIngredientResponse(BaseModel):
    user_id: int
    ingredient_id: int

    model_config = {
        "from_attributes": True
    }

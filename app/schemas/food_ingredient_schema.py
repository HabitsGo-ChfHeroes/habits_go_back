from pydantic import BaseModel

class FoodIngredientCreate(BaseModel):
    food_id: int
    ingredient_id: int

class FoodIngredientResponse(BaseModel):
    food_id: int
    ingredient_id: int

    model_config = {
        "from_attributes": True
    }

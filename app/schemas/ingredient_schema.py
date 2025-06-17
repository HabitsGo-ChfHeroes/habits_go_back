from pydantic import BaseModel

class IngredientCreate(BaseModel):
    name: str
    quantity: float
    unit: str

class IngredientResponse(BaseModel):
    id: int
    name: str
    quantity: float
    unit: str

    model_config = {
        "from_attributes": True
    }
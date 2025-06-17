from pydantic import BaseModel

class FoodCreate(BaseModel):
    name: str
    preparation: str
    video_url: str

class FoodResponse(BaseModel):
    id: int
    name: str
    preparation: str
    video_url: str

    model_config = {
        "from_attributes": True
    }
from fastapi import APIRouter
from app.schemas.plan_food_schema import PlanFoodsRequest, PlanFoodsResponse
from app.services.plan_foods_service import generate_daily_plan

router = APIRouter()

@router.post("/plan/foods", response_model=PlanFoodsResponse)
def get_plan_foods(request: PlanFoodsRequest):
    return generate_daily_plan(request)

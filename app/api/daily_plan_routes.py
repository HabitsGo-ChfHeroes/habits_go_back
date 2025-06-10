# app/api/daily_plan_routes.py

from fastapi import APIRouter
from app.schemas.daily_plan_schema import DailyPlanRequest, DailyPlanResponse
from app.services.daily_plan_service import generate_daily_plan

router = APIRouter()

@router.post("/daily-plan", response_model=DailyPlanResponse)
def get_daily_plan(request: DailyPlanRequest):
    return generate_daily_plan(request)

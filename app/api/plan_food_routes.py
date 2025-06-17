from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter
from app.schemas.plan_food_schema import DailyPlanRequest, DailyPlanResponse
from app.services.plan_foods_service import generate_daily_plan

router = APIRouter()

@router.post("/daily/plan", response_model=DailyPlanResponse)
def create_daily_plan(request: DailyPlanRequest, db: Session = Depends(get_session)):
    return generate_daily_plan(db, request)

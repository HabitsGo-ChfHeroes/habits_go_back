from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter
from app.schemas.plan_food_schema import DailyPlanRequest, DailyPlanResponseMessage, PlanFoodResponse
from app.services.plan_food_service import generate_daily_plan, update_plan_food_status_by_id, get_quantity_plan_food_completed

router = APIRouter()

@router.post("/daily/plan", response_model=DailyPlanResponseMessage)
def create_daily_plan(request: DailyPlanRequest, db: Session = Depends(get_session)):
    return generate_daily_plan(db, request)

@router.put("/{plan_food_id}/status", response_model=PlanFoodResponse)
def update_plan_food_status(plan_food_id: int, db: Session = Depends(get_session)):
    return update_plan_food_status_by_id(db, plan_food_id)

@router.get("/plan/{plan_id}/completed/meals", response_model=int)
def get_completed_quantity(plan_id: int, db: Session = Depends(get_session)):
    return get_quantity_plan_food_completed(db, plan_id)

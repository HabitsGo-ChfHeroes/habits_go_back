from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter
from app.models.plan import Plan
from app.schemas.plan_schema import PlanDetailResponse, PlanUpdate, PlanResponse
from app.services.plan_service import get_daily_plan, update_plan_comment, get_daily_plan_comment

router = APIRouter()

@router.get("/user/{user_id}/daily/plan", response_model=PlanDetailResponse)
def get_user_daily_plan(user_id: int, db: Session = Depends(get_session)):
    return get_daily_plan(db, user_id)

@router.get("/{plan_id}/comment", response_model=str)
def get_plan_comment(plan_id: int, db: Session = Depends(get_session)):
    return get_daily_plan_comment(db, plan_id)

@router.put("/{plan_id}/comment", response_model=PlanResponse)
def update_plan(plan_id: int, update_data: PlanUpdate, db: Session = Depends(get_session)):
    return update_plan_comment(db, plan_id, update_data)
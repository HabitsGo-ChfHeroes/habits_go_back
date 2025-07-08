from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_session
from fastapi import APIRouter
from app.schemas.plan_schema import PlanDetailResponse
from app.services.plan_service import get_daily_plan

router = APIRouter()

@router.get("/user/{user_id}/daily/plan", response_model=PlanDetailResponse)
def get_user_daily_plan(user_id: int, db: Session = Depends(get_session)):
    return get_daily_plan(db, user_id)

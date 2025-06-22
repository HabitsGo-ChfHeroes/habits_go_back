from sqlalchemy.orm import Session
from app.schemas.plan_schema import PlanCreate, PlanResponse
from app.repositories.plan_repository import create_plan

def create_plan_entry(db: Session, data: PlanCreate) -> PlanResponse:
    return create_plan(db, data)

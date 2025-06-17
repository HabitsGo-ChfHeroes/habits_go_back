from sqlalchemy.orm import Session
from app.models.plan import Plan
from app.schemas.plan_schema import PlanCreate, PlanResponse

def create_plan(db: Session, plan_data: PlanCreate) -> PlanResponse:
    new_plan = Plan(
        user_id = plan_data.user_id,
        date = plan_data.date
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return PlanResponse.model_validate(new_plan)

from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.plan import Plan
from app.schemas.plan_schema import PlanCreate, PlanResponse

def create_plan(plan_data: PlanCreate) -> PlanResponse:
    db: Session = next(get_session())
    new_plan = Plan(
        user_id = plan_data.user_id,
        date = plan_data.date
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)

    return PlanResponse.model_validate(new_plan)

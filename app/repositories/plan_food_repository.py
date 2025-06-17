"""
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.models.plan_food import PlanFood
from app.schemas.plan_food_schema import PlanFoodCreate, PlanFoodResponse

def create_plan_food(plan_food_data: PlanFoodCreate) -> PlanFoodResponse:
    db: Session = next(get_session())
    new_plan_food = PlanFood(
        plan_id=plan_food_data.plan_id,
        meal_id=plan_food_data.meal_id,
        food_id=plan_food_data.food_id,
        status=plan_food_data.status
    )

    db.add(new_plan_food)
    db.commit()
    db.refresh(new_plan_food)

    return PlanFoodResponse.model_validate(new_plan_food)
"""
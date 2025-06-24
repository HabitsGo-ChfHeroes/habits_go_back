from sqlalchemy.orm import Session
from app.models.plan_food import PlanFood
from app.schemas.plan_food_schema import PlanFoodCreate

def create_plan_food(db: Session, plan_food_data: PlanFoodCreate) -> PlanFood:
    new_plan_food = PlanFood(
        plan_id=plan_food_data.plan_id,
        meal_id=plan_food_data.meal_id,
        food_id=plan_food_data.food_id,
        status=plan_food_data.status
    )
    db.add(new_plan_food)
    db.commit()
    db.refresh(new_plan_food)
    return new_plan_food

def create_plan_food_uncommitted(db: Session, data: PlanFoodCreate):
    new_plan_food = PlanFood(
        plan_id=data.plan_id,
        meal_id=data.meal_id,
        food_id=data.food_id,
        status=data.status
    )
    db.add(new_plan_food)
    return new_plan_food

from sqlalchemy.orm import Session, selectinload
from datetime import date
from app.models.plan import Plan
from app.models.plan_food import PlanFood
from app.models.food import Food
from app.models.meal import Meal
from app.models.food_ingredient import FoodIngredient
from app.models.ingredient import Ingredient
from app.schemas.plan_schema import PlanCreate

def create_plan(db: Session, plan_data: PlanCreate) -> Plan:
    new_plan = Plan(
        user_id=plan_data.user_id,
        date=plan_data.date
    )
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan

def create_plan_uncommitted(db: Session, plan_data: PlanCreate) -> Plan:
    new_plan = Plan(
        user_id=plan_data.user_id,
        date=plan_data.date
    )
    db.add(new_plan)
    db.flush()
    return new_plan

def get_full_plan_by_user_and_date(db: Session, user_id: int, today: date):
    return (
        db.query(Plan)
        .filter(Plan.user_id == user_id, Plan.date == today)
        .options(
            selectinload(Plan.plan_foods)
            .selectinload(PlanFood.food)
            .selectinload(Food.food_ingredients)
            .selectinload(FoodIngredient.ingredient),
            selectinload(Plan.plan_foods)
            .selectinload(PlanFood.meal)
        )
        .first()
    )
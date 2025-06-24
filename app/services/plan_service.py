from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.utils.time_utils import get_today_lima
from app.schemas.plan_schema import PlanCreate, PlanResponse, PlanDetailResponse, PlanMealIngredient, PlanMeal, PlanMealFood
from app.repositories.plan_repository import create_plan, create_plan_uncommitted, get_full_plan_by_user_and_date, exists_plan_by_user_and_date

def create_plan_entry(db: Session, data: PlanCreate) -> PlanResponse:
    plan = create_plan(db, data)
    return PlanResponse.model_validate(plan)

def create_plan_entry_uncommitted(db: Session, data: PlanCreate):
    if exists_plan_by_user_and_date(db, data.user_id, data.date):
        raise HTTPException(status_code=400, detail="Ya existe un plan para este usuario en esta fecha")
    
    return create_plan_uncommitted(db, data)

def get_daily_plan(db: Session, user_id: int) -> PlanDetailResponse:
    plan = get_full_plan_by_user_and_date(db, user_id, get_today_lima())
    if not plan:
        raise HTTPException(status_code=404, detail="No se encontró plan para hoy")

    meals = []
    for pf in plan.plan_foods:
        food = pf.food
        meal = pf.meal
        ingredients = [
            PlanMealIngredient(
                name=fi.ingredient.name,
                quantity=fi.ingredient.quantity,
                unit=fi.ingredient.unit
            )
            for fi in food.food_ingredients
        ]

        meals.append(PlanMeal(
            plan_food_id=pf.id,
            name=meal.name,
            hour=meal.hour,
            food=PlanMealFood(
                name=food.name,
                preparation=food.preparation,
                video_url=food.video_url,
                ingredients=ingredients
            ),
            status=pf.status
        ))

    return PlanDetailResponse(
        date=plan.date,
        meals=meals
    )

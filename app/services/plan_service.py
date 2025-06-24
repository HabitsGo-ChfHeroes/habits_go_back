from sqlalchemy.orm import Session
from datetime import date
from app.schemas.plan_schema import PlanCreate, PlanResponse, PlanDetailResponse, PlanMealIngredient, PlanMeal, PlanMealFood
from app.repositories.plan_repository import create_plan, get_full_plan_by_user_and_date

def create_plan_entry(db: Session, data: PlanCreate) -> PlanResponse:
    plan = create_plan(db, data)
    return PlanResponse.model_validate(plan)

def get_daily_plan(db: Session, user_id: int) -> PlanDetailResponse:
    plan = get_full_plan_by_user_and_date(db, user_id, date.today())
    if not plan:
        raise ValueError("No se encontró plan para hoy")

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

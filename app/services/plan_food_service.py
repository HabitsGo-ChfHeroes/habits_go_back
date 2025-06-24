from sqlalchemy.orm import Session
from datetime import date, time
from app.schemas.plan_food_schema import DailyPlanRequest, DailyPlanResponseMessage, PlanFoodCreate, PlanFoodResponse
from app.schemas.food_schema import FoodCreate
from app.schemas.ingredient_schema import IngredientCreate
from app.schemas.meal_schema import MealCreate
from app.schemas.plan_schema import PlanCreate
from app.schemas.food_ingredient_schema import FoodIngredientCreate
from app.services.openai_service import generate_recipe
from app.services.user_service import get_user_details_by_id
from app.services.food_service import create_food_entry_uncommitted
from app.services.ingredient_service import create_ingredient_entry_uncommitted
from app.services.meal_service import create_meal_entry_uncommitted
from app.services.plan_service import create_plan_entry_uncommitted
from app.services.food_ingredient_service import create_food_ingredient_entry_uncommitted
from app.repositories.plan_food_repository import create_plan_food_uncommitted, get_plan_food_by_id, update_status
from app.enums.meal_type import MealTypeEnum
from app.enums.status import Status

def generate_daily_plan(db: Session, request: DailyPlanRequest) -> DailyPlanResponseMessage:
    today = date.today()

    user_details = get_user_details_by_id(db, request.user_id)

    plan = create_plan_entry_uncommitted(db, PlanCreate(
        user_id=user_details.id,
        date=today
    ))

    for enum_meal_type in MealTypeEnum:
        recipe = generate_recipe(enum_meal_type.value, user_details.goal.value)

        food = create_food_entry_uncommitted(db, FoodCreate(
            name=recipe["food"]["name"],
            preparation=recipe["food"]["preparation"],
            video_url=recipe["food"]["video_url"]
        ))

        meal_time = time.fromisoformat(recipe["food"]["time"])
        meal = create_meal_entry_uncommitted(db, MealCreate(
            name=enum_meal_type,
            hour=meal_time
        ))

        for ing in recipe["ingredients"]:
            ingredient = create_ingredient_entry_uncommitted(db, IngredientCreate(
                name=ing["name"],
                quantity=ing["quantity"] or 0,
                unit=ing["unit"]
            ))
            create_food_ingredient_entry_uncommitted(db, FoodIngredientCreate(
                food_id=food.id,
                ingredient_id=ingredient.id
            ))

        create_plan_food_uncommitted(db, PlanFoodCreate(
            plan_id=plan.id,
            meal_id=meal.id,
            food_id=food.id,
            status=Status.NOT_COMPLETED
        ))

    db.commit()

    return DailyPlanResponseMessage(message="Plan diario generado exitosamente")

def update_plan_food_status_by_id(db: Session, plan_food_id: int) -> PlanFoodResponse:
    plan = get_plan_food_by_id(db, plan_food_id)
    if plan:
        plan.status = Status.NOT_COMPLETED if plan.status == Status.COMPLETED else Status.COMPLETED
        updated = update_status(db, plan)
        return PlanFoodResponse.model_validate(updated)
    return PlanFoodResponse.model_validate(updated)

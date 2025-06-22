from sqlalchemy.orm import Session
from datetime import date, time
from app.models.food import Food
from app.models.ingredient import Ingredient
from app.models.meal import Meal
from app.schemas.plan_food_schema import DailyPlanRequest, DailyPlanResponse, PlanFoodCreate
from app.schemas.food_schema import FoodCreate
from app.schemas.ingredient_schema import IngredientCreate
from app.schemas.meal_schema import MealCreate
from app.schemas.plan_schema import PlanCreate
from app.schemas.food_ingredient_schema import FoodIngredientCreate
from app.services.openai_service import generate_recipe
from app.services.user_service import get_user_details_by_id
from app.services.food_service import create_food_entry
from app.services.ingredient_service import create_ingredient_entry
from app.services.meal_service import create_meal_entry
from app.services.plan_service import create_plan_entry
from app.services.food_ingredient_service import create_food_ingredient_entry
from app.repositories.plan_food_repository import create_plan_food
from app.enums.meal_type import MealTypeEnum
from app.enums.status import Status

def generate_daily_plan(db: Session, request: DailyPlanRequest) -> DailyPlanResponse:
    today = date.today()

    user_details = get_user_details_by_id(db, request.user_id)

    plan = create_plan_entry(db, PlanCreate(
        user_id=user_details.id,
        date=today
    ))

    for enum_meal_type in MealTypeEnum:
        recipe = generate_recipe(enum_meal_type.value, user_details.goal.value)

        food = create_food_entry(db, FoodCreate(
            name=recipe["food"]["name"],
            preparation=recipe["food"]["preparation"],
            video_url=recipe["food"]["video_url"]
        ))

        meal_time = time.fromisoformat(recipe["food"]["time"])
        meal = create_meal_entry(db, MealCreate(
            name=enum_meal_type,
            hour=meal_time
        ))

        ingredient_objs = []
        for ing in recipe["ingredients"]:
            ingredient = create_ingredient_entry(db, IngredientCreate(
                name=ing["name"],
                quantity=ing["quantity"] or 0,
                unit=ing["unit"]
            ))
            create_food_ingredient_entry(db, FoodIngredientCreate(
                food_id=food.id,
                ingredient_id=ingredient.id
            ))
            ingredient_objs.append(Ingredient(**ingredient.model_dump()))

        create_plan_food(db, PlanFoodCreate(
            plan_id=plan.id,
            meal_id=meal.id,
            food_id=food.id,
            status=Status.NOT_COMPLETED
        ))

    return DailyPlanResponse(message = "Plan diario generado exitosamente")
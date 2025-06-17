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
from app.repositories.plan_repository import create_plan
from app.repositories.food_repository import create_food
from app.repositories.ingredient_repository import create_ingredient
from app.repositories.food_ingredient_repository import create_food_ingredient
from app.repositories.meal_repository import create_meal
from app.repositories.plan_food_repository import create_plan_food
from app.enums.meal_type import MealTypeEnum
from app.enums.status import Status

def generate_daily_plan(db: Session, request: DailyPlanRequest) -> DailyPlanResponse:
    today = date.today()

    # Crear el plan para el usuario
    plan = create_plan(db, PlanCreate(
        user_id=request.user_id,
        date=today
    ))

    for enum_meal_type in MealTypeEnum:
        # Generar receta desde OpenAI (se pasa el string del enum)
        recipe = generate_recipe(enum_meal_type.value, request.goal)

        # Crear la comida (Food)
        food = create_food(db, FoodCreate(
            name=recipe["food"]["name"],
            preparation=recipe["food"]["preparation"],
            video_url=recipe["food"]["video_url"]
        ))

        # Crear el tipo de comida (Meal)
        meal_time = time.fromisoformat(recipe["food"]["time"])
        meal = create_meal(db, MealCreate(
            name=enum_meal_type,
            hour=meal_time
        ))

        # Crear los ingredientes y sus relaciones
        ingredient_objs = []
        for ing in recipe["ingredients"]:
            ingredient = create_ingredient(db, IngredientCreate(
                name=ing["name"],
                quantity=ing["quantity"] or 0,
                unit=ing["unit"]
            ))
            create_food_ingredient(db, FoodIngredientCreate(
                food_id=food.id,
                ingredient_id=ingredient.id
            ))
            ingredient_objs.append(Ingredient(**ingredient.model_dump()))

        # Crear la relación PlanFood
        create_plan_food(db, PlanFoodCreate(
            plan_id=plan.id,
            meal_id=meal.id,
            food_id=food.id,
            status=Status.NOT_COMPLETED
        ))

    return DailyPlanResponse(message = "Plan diario generado exitosamente")
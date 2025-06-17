from app.schemas.plan_food_schema import PlanFoodsRequest, PlanFoodsResponse
from app.services.openai_service import generate_recipe

def generate_daily_plan(request: PlanFoodsRequest) -> PlanFoodsResponse:
    meal_types = ["Desayuno", "Media mañana", "Almuerzo", "Merienda", "Cena"]
    meals = [generate_recipe(meal, request.goal) for meal in meal_types]
    return PlanFoodsResponse(meals=meals)
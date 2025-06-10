# app/services/daily_plan_service.py

from app.schemas.daily_plan_schema import Meal, DailyPlanResponse, DailyPlanRequest
import requests

def generate_recipe_with_ollama(meal_type: str, goal: str) -> Meal:
    prompt = f"""Eres un nutricionista. Dame una receta para {meal_type} para alguien cuyo objetivo es '{goal}'.
Devuélvela con:
- Nombre del plato
- Ingredientes
- Preparación
- Un link corto de un video (puedes inventarlo)

No repitas platos entre comidas."""

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "mistral",  # o llama3, si usas otro
            "prompt": prompt,
            "stream": False
        })
        result = response.json()["response"]

        # Aquí harás un parseo real más adelante.
        return Meal(
            type=meal_type,
            dishName=f"{meal_type} generado",
            ingredients=result,
            preparation="Por definir",
            videoUrl="https://example.com"
        )
    except Exception as e:
        return Meal(
            type="Error",
            dishName="No se pudo generar",
            ingredients=str(e),
            preparation="",
            videoUrl=""
        )

def generate_daily_plan(request: DailyPlanRequest) -> DailyPlanResponse:
    meal_types = ["Desayuno", "Media mañana", "Almuerzo", "Merienda", "Cena"]
    meals = [generate_recipe_with_ollama(meal, request.goal) for meal in meal_types]
    return DailyPlanResponse(meals=meals)

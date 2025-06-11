# app/services/daily_plan_service.py

from app.schemas.daily_plan_schema import Meal, DailyPlanResponse, DailyPlanRequest
import requests
import re

def parse_response(text: str, meal_type: str) -> Meal:
    try:
        # Intentar extraer el nombre del plato de diferentes formas
        name_match = re.search(r"\*\*(Nombre del plato|Plato):\*\*\s*(.*?)\n", text)
        if not name_match:
            alt_name_match = re.search(r"^\s*(.*?)\n", text)
            name = alt_name_match.group(1).strip() if alt_name_match else "Nombre no encontrado"
        else:
            name = name_match.group(2).strip()

        ingredients_match = re.search(r"\*\*Ingredientes:\*\*\n(.+?)(\n\n|\Z)", text, re.DOTALL)
        preparation_match = re.search(r"\*\*Preparación:\*\*\n(.+?)(\n\n|\Z)", text, re.DOTALL)
        video_match = re.search(r"\*\*(Video|Link al video):\*\*\s*\[.*?\]\((.*?)\)", text)

        return Meal(
            type=meal_type,
            dishName=name,
            ingredients=ingredients_match.group(1).strip() if ingredients_match else "Ingredientes no encontrados",
            preparation=preparation_match.group(1).strip() if preparation_match else "Preparación no encontrada",
            videoUrl=video_match.group(2).strip() if video_match else "https://example.com"
        )
    except Exception as e:
        return Meal(
            type="Error",
            dishName="Error en el parseo",
            ingredients=str(e),
            preparation="",
            videoUrl=""
        )

def generate_recipe_with_ollama(meal_type: str, goal: str) -> Meal:
    prompt = f"""Eres un nutricionista profesional. Responde exclusivamente en español. No incluyas introducciones, saludos, ni frases explicativas.

        Debes generar una receta para {meal_type} que ayude a una persona cuyo objetivo es '{goal}'.
        Responde usando estrictamente este formato:
        **Nombre del plato:** (solo el nombre del platillo, sin frases adicionales)
        **Ingredientes:**
        - Lista de ingredientes (uno por línea, usando viñetas)
        **Preparación:**
        Pasos detallados de la preparación
        **Video:** [Link al video](https://...) (puede ser ficticio si no existe)"""

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        })
        raw_text = response.json()["response"]
        return parse_response(raw_text, meal_type)
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

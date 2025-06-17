from openai import OpenAI
from dotenv import load_dotenv
import os
import re
from typing import Dict
from youtube_service import find_youtube_video_url

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_ingredient_text(ingredient_text: str) -> Dict:
    match = re.match(r"(?P<quantity>[\d/.]+)\s*(?P<unit>\w+)?\s+de\s+(?P<name>.+)", ingredient_text, re.IGNORECASE)
    if match:
        return {
            "name": match.group("name").strip(),
            "quantity": float(eval(match.group("quantity"))),
            "unit": match.group("unit") or ""
        }
    else:
        return {
            "name": ingredient_text.strip(),
            "quantity": None,
            "unit": ""
        }

def parse_recipe_response(response_text: str) -> dict:
    name_match = re.search(r"\*\*Nombre del plato:\*\*\s*(.+)", response_text)
    ingredients_match = re.search(r"\*\*Ingredientes:\*\*\s*(.*?)\*\*Preparación:\*\*", response_text, re.DOTALL)
    preparation_match = re.search(r"\*\*Preparación:\*\*\s*(.+)", response_text, re.DOTALL)

    name = name_match.group(1).strip() if name_match else ""
    
    raw_ingredients = ingredients_match.group(1).strip().splitlines() if ingredients_match else []
    parsed_ingredients = [parse_ingredient_text(line.strip("- ").strip()) for line in raw_ingredients]

    preparation = preparation_match.group(1).strip() if preparation_match else ""

    return {
        "food": {
            "name": name,
            "preparation": preparation,
            "video_url": find_youtube_video_url(name) if name else "https://example.com"
        },
        "ingredients": parsed_ingredients
    }

def generate_recipe_text(meal_type: str, goal_type: str) -> dict:
    prompt = f"""Eres un nutricionista profesional. Responde exclusivamente en español. No incluyas introducciones, saludos, ni frases explicativas.

            Debes generar una receta para {meal_type} que ayude a una persona cuyo objetivo es {goal_type}.
            Responde usando estrictamente este formato:
            **Nombre del plato:** (solo el nombre del platillo, sin frases adicionales)
            **Ingredientes:**
            - Lista de ingredientes (uno por línea, usando viñetas)
            - Debes usar exactamente este formato: 'cantidad' 'unidad' de 'ingrediente'
            - Si no hay unidad, usa la palabra "unidad" o "unidades"
            - Incorrecto: 1 plátano
            - Correcto: 1 unidad de plátano
            - Correcto: 200 ml de leche desnatada
            **Preparación:**
            Pasos detallados de la preparación"""
    
    response = client.responses.create(
        model = "gpt-4o-mini",
        input = prompt,
        temperature = 1.2
    )

    return parse_recipe_response(response.output_text)

result = generate_recipe_text("media mañana", "bajar de peso")
print(result)
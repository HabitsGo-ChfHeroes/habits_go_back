import requests

def generate_recipe_with_ollama(goal: str, meal_type: str):
    prompt = (
        f"Genera una receta saludable para {meal_type} que ayude a una persona cuyo objetivo es '{goal}'. "
        f"Incluye el nombre del plato, ingredientes, preparación y un enlace a un video de YouTube si es posible."
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    if response.status_code != 200:
        return {
            "type": "Error",
            "dishName": "Error al generar",
            "ingredients": f"Error: {response.text}",
            "preparation": "Verifica que Ollama esté corriendo.",
            "videoUrl": ""
        }

    generated_text = response.json()["response"]

    # Aquí puedes procesar mejor el texto generado si deseas
    return {
        "type": meal_type,
        "dishName": "Generado por IA",
        "ingredients": generated_text,
        "preparation": "",
        "videoUrl": ""
    }
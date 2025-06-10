# app/services/ollama_service.py
import requests

def ask_ollama(prompt: str, model: str = "llama3") -> str:
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        raise RuntimeError(f"Ollama error: {str(e)}")

from fastapi import FastAPI
from src.config import API_KEY
from src.clima import get_clima

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API de clima funcionando"}

@app.get("/clima/{ciudad}")
def clima(ciudad: str):
    try:
        datos = get_clima(ciudad, API_KEY)
        return {
            "ciudad": datos["name"],
            "temperatura": datos["main"]["temp"],
            "descripcion": datos["weather"][0]["description"]
        }
    except Exception as e:
        return {"error": str(e)}
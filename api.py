from fastapi import FastAPI
from src.config import API_KEY
from src.clima import get_clima
from src.database import guardar_registro, obtener_registros, obtener_por_ciudad

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

@app.post("/clima/{ciudad}")
def guardar_clima_db(ciudad: str):
    try:
        datos = get_clima(ciudad, API_KEY)
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        guardar_registro(ciudad, temp, descripcion)
        return {"mensaje": f"Registro guardado para {ciudad}"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/registros")
def ver_registros():
    registros = obtener_registros()
    return [{"id": r.id, "ciudad": r.ciudad, "temperatura": r.temperatura, 
             "descripcion": r.descripcion, "fecha": str(r.fecha)} for r in registros]

@app.get("/registros/{ciudad}")
def ver_por_ciudad(ciudad: str):
    registros = obtener_por_ciudad(ciudad)
    return [{"id": r.id, "ciudad": r.ciudad, "temperatura": r.temperatura,
             "descripcion": r.descripcion, "fecha": str(r.fecha)} for r in registros]
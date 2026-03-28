from src.config import API_KEY
from src.clima import get_clima

try:
    datos = get_clima("jaisdnj", API_KEY)
    temp=datos["main"]['temp']
    descripción=datos["weather"][0]["description"]
    ciudad=datos["name"]
    print(f"en {ciudad} hay una temperatura de {temp}C° y un éstado general: {descripción} ")
except Exception as e:
    print(f"Error al consultar el clima: {e}")
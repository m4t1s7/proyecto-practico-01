from src.config import API_KEY
from src.clima import get_clima
from src.datos import save_weather, leer_registros, filtrar_por_ciudad

ciudad=input("de qué ciudad quieres saber el clima?: ")

try:
    datos = get_clima(ciudad, API_KEY)
    temp=datos["main"]['temp']
    descripción=datos["weather"][0]["description"]
    ciudad=datos["name"]
    print(f"en {ciudad} hay una temperatura de {temp}C° y un éstado general: {descripción} ")
    save_weather(ciudad, temp, descripción)
    df = leer_registros()
    print(df)
    print(f"\nTemperatura promedio: {df['temperatura'].mean():.1f}°C")
    print(filtrar_por_ciudad(ciudad))
    
except Exception as e:
    print(f"Error al consultar el clima: {e}")


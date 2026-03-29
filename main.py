from src.config import API_KEY
from src.clima import get_clima
from src.datos import save_weather, leer_registros, filtrar_por_ciudad
from src.logger import get_logger

ciudad=input("de qué ciudad quieres saber el clima?: ")
logger = get_logger("main")

try:
    datos = get_clima(ciudad, API_KEY)
    temp=datos["main"]['temp']
    descripción=datos["weather"][0]["description"]
    ciudad=datos["name"]
    logger.info(f"en {ciudad} hay una temperatura de {temp}C° y un éstado general: {descripción} ")
    save_weather(ciudad, temp, descripción)
    df = leer_registros()
    logger.info(df)
    logger.info(f"\nTemperatura promedio: {df['temperatura'].mean():.1f}°C")
    logger.info(filtrar_por_ciudad(ciudad))
    
except Exception as e:
    logger.error(f"Error al consultar el clima: {e}")


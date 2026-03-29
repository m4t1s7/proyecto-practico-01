import schedule
import time
from src.config import API_KEY
from src.clima import get_clima
from src.datos import save_weather
from src.logger import get_logger

logger = get_logger("automatizar")

def consulta_automatica():
    ciudad = "Chia"
    try:
        datos = get_clima(ciudad, API_KEY)
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        save_weather(ciudad, temp, descripcion)
        logger.info(f"Consulta automática exitosa para {ciudad}")
    except Exception as e:
        logger.error(f"Error en consulta automática: {e}")

schedule.every(1).minutes.do(consulta_automatica)

logger.info("Automatización iniciada")

while True:
    schedule.run_pending()
    time.sleep(1)
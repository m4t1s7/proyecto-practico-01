import pandas as pd
from datetime import datetime

def save_weather(ciudad: str, temp: str, descripcion: str ) -> None:
    datos = {
        "ciudad" : [ciudad],
        "temperatura" : [temp],
        "descripción" : [descripcion],
        "fecha" : [datetime.now().strftime("%Y-%m-%d %H:%M")]
    }
    df = pd.DataFrame(datos)
    df.to_csv("clima_registros.csv", mode="a", header=False, index=False)
    print(f"Registro guardado para {ciudad}")

def leer_registros() -> pd.DataFrame:
    df = pd.read_csv("clima_registros.csv", 
                     names=["ciudad", "temperatura", "descripcion", "fecha"])
    return df

def filtrar_por_ciudad(ciudad: str) -> pd.DataFrame:
    df = leer_registros()
    return df[df["ciudad"] == ciudad]
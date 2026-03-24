#Ésta función hará el proceso de convertir unidades
def convertir(unidad: str, valor: float, equivalencias: dict) -> float:
    return valor*equivalencias[unidad]
#Ésta función referenciará la medida a la cual convertimos
def comparar(unidad_a_convertir: str,comparadas: dict) -> str:
    return comparadas[unidad_a_convertir]
def limpiar(texto: str) -> str:
    reemplazos = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"}
    texto = texto.lower()
    for tilde, sin_tilde in reemplazos.items():
        texto = texto.replace(tilde, sin_tilde)
    return texto
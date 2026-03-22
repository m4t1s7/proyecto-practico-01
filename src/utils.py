#Ésta función hará el proceso de convertir unidades
def convertir(unidad: str, valor: float, equivalencias: dict) -> float:
    return valor*equivalencias[unidad]
#Ésta función referenciará la medida a la cual convertimos
def comparar(unidad_a_convertir: str,comparadas: dict) -> str:
    return comparadas[unidad_a_convertir]
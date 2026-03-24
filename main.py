from src.config import equivalencias, comparadas
from src.utils import convertir, comparar, limpiar

unidad_a_convertir=limpiar(input("Qué unidad quieres convertir?(escribela en minuscula)(elige entre kilogramo, libra, kilometro, milla, acre y hectarea): ")) #Solicitamos la unidad de medida que buscaremos convertir
valor_unidad_a_convertir=float(input("ahora introduce el valor de esa unidad: "))#Acá sabemos la cantidad de unidades

print(f"listo, tu conversión resulta en que {valor_unidad_a_convertir} {unidad_a_convertir} equivalen a", convertir(unidad_a_convertir, valor_unidad_a_convertir, equivalencias), comparar(unidad_a_convertir,comparadas))
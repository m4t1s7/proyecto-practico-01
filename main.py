from src.config import kilogramo, libra, kilometro, milla, acre, hectarea, equivalencias
from src.utils import convertir

unidad_a_cambiar=input("Qué unidad quieres convertir?(escribela en minuscula)(elige entre kilogramo, libra, kilometro, milla, acre y hectarea): ")
valor_unidad_a_cambiar=int(input("ahora introduce el valor de esa unidad: "))

print(convertir(valor_unidad_a_cambiar, equivalencias[unidad_a_cambiar]))
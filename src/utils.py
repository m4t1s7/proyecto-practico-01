def convertir(unidad_a_convertir, valor_unidad_a_convertir, equivalencias: dict) -> float:
    for equivalencia in equivalencias.keys():
        if unidad_a_convertir==equivalencia:
            conversión=valor_unidad_a_convertir*equivalencias[equivalencia]
    return conversión
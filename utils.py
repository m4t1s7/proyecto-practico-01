def convertir(valor_unidad_a_cambiar, unidad_a_cambiar, kilogramo, libra, kilometro, milla, acre, hectarea):
    if unidad_a_cambiar=="kilogramo":
        nueva=valor_unidad_a_cambiar*libra
        print(f"listo, {valor_unidad_a_cambiar, unidad_a_cambiar} equivalen a {nueva} libras")
    if unidad_a_cambiar=="libra":
        nueva=valor_unidad_a_cambiar*kilogramo
        print(f"listo, {valor_unidad_a_cambiar, unidad_a_cambiar} equivalen a {nueva} kilogramos")
    if unidad_a_cambiar=="kilometro":
        nueva=valor_unidad_a_cambiar*milla
        print(f"listo, {valor_unidad_a_cambiar, unidad_a_cambiar} equivalen a {nueva} millas")
    if unidad_a_cambiar=="milla":
        nueva=valor_unidad_a_cambiar*kilometro
        print(f"listo, {valor_unidad_a_cambiar, unidad_a_cambiar} equivalen a {nueva} kilometros")
    if unidad_a_cambiar=="acre":
        nueva=valor_unidad_a_cambiar*hectarea
        print(f"listo, {valor_unidad_a_cambiar, unidad_a_cambiar} equivalen a {nueva} hectareas")
    if unidad_a_cambiar=="hectarea":
        nueva=valor_unidad_a_cambiar*acre
        print(f"listo, {valor_unidad_a_cambiar, unidad_a_cambiar} equivalen a {nueva} acres")
    
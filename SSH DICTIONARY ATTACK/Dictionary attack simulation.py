diccionario = ["1234", "4566", "6564", "65"]

intento_ataque = "65645464"

i = 4566

for i in diccionario:
    if i==intento_ataque:
        print(f"Contraseña correcta detectada: {intento_ataque}. Scanner finalizado. ")
        exit()
    else:
        print(f"La contraseña {i} no es válida.")
else:
    print(f"No se han detectado coincidencias.")
    exit()
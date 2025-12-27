import hashlib

# 1. Función para convertir texto en hash
def generar_hash(password):
    hash_resultante = hashlib.sha256(password.encode()).hexdigest()
    return hash_resultante

# 2. Base de datos en memoria (se borra al cerrar el programa)
base_de_datos = {}

# 3. Función de Registro
def registrar_usuario():
    usuario = input("Elige un nombre de usuario: ")
    password = input("Elige una contraseña: ")
    base_de_datos[usuario] = generar_hash(password)
    print(f"✅ Usuario '{usuario}' registrado con éxito!")

# 4. Función de Login
def login():
    print("\n--- Inicio de sesión ---")
    usuario_ingresado = input("Usuario: ")
    password_ingresada = input("Contraseña: ")

    if usuario_ingresado in base_de_datos:
        hash_ingresado = generar_hash(password_ingresada)
        if hash_ingresado == base_de_datos[usuario_ingresado]:
            print("🔓 Acceso concedido. Bienvenido al sistema.")
        else:
            print("❌ Contraseña incorrecta. Acceso denegado.")
    else:
        print("⚠️ El usuario no existe.")

# --- AQUÍ ESTÁ EL MENÚ INTERACTIVO ---

while True:
    print("\n========= MI SISTEMA SEGURO =========")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Ver base de datos (Hashes)")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        login()
    elif opcion == "3":
        print(f"\nEstado actual de la memoria: {base_de_datos}")
    elif opcion == "4":
        print("Saliendo del sistema... ¡Adiós!")
        break # Esto rompe el bucle y cierra el programa
    else:
        print("Opción no válida, intenta de nuevo.")
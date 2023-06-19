def aplicacion_1():
    # Código de la primera aplicación
    print("Aplicación 1")

def aplicacion_2():
    # Código de la segunda aplicación
    print("Aplicación 2")

def aplicacion_3():
    # Código de la tercera aplicación
    print("Aplicación 3")

def aplicacion_4():
    # Código de la cuarta aplicación
    print("Aplicación 4")

def seleccionar_aplicacion():
    print("Selecciona una aplicación:")
    print("1. Aplicación 1")
    print("2. Aplicación 2")
    print("3. Aplicación 3")
    print("4. Aplicación 4")

    opcion = input("Ingresa el número de la aplicación que deseas ejecutar: ")

    if opcion == "1":
        aplicacion_1()
    elif opcion == "2":
        aplicacion_2()
    elif opcion == "3":
        aplicacion_3()
    elif opcion == "4":
        aplicacion_4()
    else:
        print("Opción inválida. Por favor, selecciona un número válido.")

# Programa principal
seleccionar_aplicacion()

import os

def gestionar_lista(nombre_archivo):
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
        archivo = open(nombre_archivo, 'w')
        archivo.close()
    
    while True:
        print("\n--- GESTIONAR LISTA ---")
        print("1. Ver la lista")
        print("2. Actualizar la lista")
        print("3. Eliminar la lista")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            ver_lista(nombre_archivo)
        elif opcion == '2':
            actualizar_lista(nombre_archivo)
        elif opcion == '3':
            eliminar_lista(nombre_archivo)
        elif opcion == '0':
            break
        else:
            print("Opción inválida. Por favor, intenta nuevamente.")

def ver_lista(nombre_archivo):
    print("\n--- VER LISTA ---")
    
    # Leer el contenido del archivo
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    
    if contenido:
        print(contenido)
    else:
        print("La lista está vacía.")

def actualizar_lista(nombre_archivo):
    print("\n--- ACTUALIZAR LISTA ---")
    
    # Leer el contenido actual del archivo
    with open(nombre_archivo, 'r') as archivo:
        contenido_actual = archivo.read()
    
    print("Contenido actual de la lista:")
    print(contenido_actual)
    
    # Solicitar al usuario la nueva entrada para la lista
    nueva_entrada = input("Ingresa la nueva entrada para la lista: ")
    
    # Actualizar el contenido del archivo
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido_actual + '\n' + nueva_entrada)
    
    print("La lista ha sido actualizada correctamente.")

def eliminar_lista(nombre_archivo):
    print("\n--- ELIMINAR LISTA ---")
    
    # Confirmar la eliminación de la lista
    confirmacion = input("¿Estás seguro de que deseas eliminar la lista? (s/n): ")
    
    if confirmacion.lower() == 's':
        # Eliminar el archivo
        os.remove(nombre_archivo)
        print("La lista ha sido eliminada correctamente.")
    else:
        print("Eliminación de lista cancelada.")

# Ejemplo de uso de la función
gestionar_lista("mi_lista.txt")

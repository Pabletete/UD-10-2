
from os import system
system('clear')

import random

def trabajar_con_listas(n):
    lista = []
    
    # Generar una lista de números aleatorios
    for _ in range(n):
        numero_aleatorio = random.randint(1, 100)
        lista.append(numero_aleatorio)
    
    # Imprimir la lista generada
    print("Lista generada:", lista)
    
    # Sumar todos los elementos de la lista
    suma = sum(lista)
    print("Suma de los elementos:", suma)
    
    # Calcular el promedio de la lista
    promedio = suma / len(lista)
    print("Promedio de la lista:", promedio)
    
    # Encontrar el valor máximo y mínimo en la lista
    maximo = max(lista)
    minimo = min(lista)
    print("Valor máximo:", maximo)
    print("Valor mínimo:", minimo)
    
    # Ordenar la lista de forma ascendente
    lista.sort()
    print("Lista ordenada:", lista)
    
    # Comprobar si un número dado está en la lista
    numero = random.randint(1, 100)
    if numero in lista:
        print(f"El número {numero} está en la lista.")
    else:
        print(f"El número {numero} no está en la lista.")

# Ejemplo de uso de la función
trabajar_con_listas(10)

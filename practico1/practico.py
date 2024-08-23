#import numpy as np
#Escribir un programa que pida al usuario su nombre y lo salude. Pista: van a necesitar la función input().
"""
def pedirNombre():
    print("Como te llamas? ")
    nombre = input()
    print(f"Hola {nombre} !")
"""
    
#Crear una función que devuelva la suma de dos números.
"""
def sumar(num1,num2):
    result = num1 + num2
    return result
num1 = int(input())
num2 = int(input())
sumar(num1,num2)
"""

#Escribir un programa que calcule el área de un círculo dado su radio.2
"""
def areaCirculo(r):
    return np.pi * r **2
r = int(input())
print(areaCirculo(r))
"""

#Crear una lista de 5 frutas y escribir un bucle que las imprima una por una.
"""
def cargarLista(lista):
    for i in range(0,5):
        print(f"Agregar fruta {i}: ")
        fruta = input()
        lista.append(fruta)

def mostrarLista(lista):
    for i in lista:
        print(i)

lista = []
cargarLista(lista)
mostrarLista(lista)
"""
"""
# Escribir una función que determine si un número es par o impar.

def parOimpar(numero):
    if numero % 2  == 0:
        return True
    else:
        return False

numero = int(input())
print(parOimpar(numero))
"""
"""
1. entrar al directorio cd .\Desktop\ 
2. entrar al practico1\Scripts\activate  
3. python practico.py para correr el programa
"""
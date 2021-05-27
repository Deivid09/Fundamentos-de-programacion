# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:47:56 2021

@author: trausch
"""

#programa lee una tabla y la imprime desde el 1 hasta el 20 y suma resultado

#declarar variables
tabla = 0
multiplicador = 1
resultado = 0
sumaResultado = 0
conRepCiclo = 1

#leer el numero de la tabla para la cual vamos a realizar las operaciones
tabla = int(input("Tabla : "))
#Leer el multiplicador
multiplicador = int(input("Ingrese Multiplicador : "))
#inicio el ciclo repetitivo que se llama FOR
for conRepCiclo in range (multiplicador +1):
    resultado = tabla * conRepCiclo
    sumaResultado = resultado + sumaResultado
    print (tabla, " * ", conRepCiclo, " = ", resultado)
#se imprime la suma por fuera de ciclo
print ("La suma del los resultados es : ", sumaResultado)
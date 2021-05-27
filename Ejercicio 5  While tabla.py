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
#inicio el ciclo repetitivo que se llama WHILE
while (conRepCiclo <= multiplicador):
    resultado = tabla * conRepCiclo
    sumaResultado = resultado + sumaResultado
    print (tabla, " * ", conRepCiclo, " = ", resultado)
    #incrementar la variable que controla el ciclo
    conRepCiclo = conRepCiclo + 1
#finaliza ciclo para la impresion del ultimo resultado    
print ("La suma de los resultados es: ", sumaResultado)
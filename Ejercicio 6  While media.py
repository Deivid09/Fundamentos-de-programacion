# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:54:40 2021

@author: trausch
"""

#Determinar la lista de un numero indefinido de positivos terminados con un numero negativo
# programa que lee N numeros enteros y calcula su promedio sale con un numero menor a cero

#declarar variables

num = 0 #variable que almacena los numeros que digita el usuario
sum = 0 #variable que suma los numeros que digita el usuario
med = 0.0  #variable que almacena la media
canEle = 0  #variable que almacena la cantidad de cantidad de numeros ingrasados por el usuario

# entrada
num = int(input ("Numero : "))  #lectura del primer numero


while (num > 0):   #condicion mientras inicia ciclo
    sum = sum + num    #operacion 
    num = int(input("Numero : "))   #lectura de los otros numeros
    canEle = canEle + 1    # contador de proceso
    
#termina ciclo
if canEle != 0:
    med = sum/canEle    #calcular media
    print("La media es :", med)   #imprimir la media
else :
    print ("No hay numeros para calcular la media")
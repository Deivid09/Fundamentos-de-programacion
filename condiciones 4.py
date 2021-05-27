# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:12:19 2021

@author: trausch
"""
# imprimir los 3 numeros  
print("ingrese 3 numeros enteros diferenetes")
# ingresar la opcion a realizar dependiendo de lo que necesite
e = int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor : "))
# ingrese los numeros que solicita el problema
a = int(input("ingrese el numero a : "))
b = int(input("ingrese el numero b : "))
c = int(input("ingrese el numero c : "))


# Si la variabel e es igual y solo igual a 1 por el verdadero
if (e == 1):  
    # si la variable a es mayor a b por el verdadero
    if (a > b):
        #si la variable a es mayor que c por el verdadero
        if (a > c):
            # si la variable b es maor que c por verdadero
            if(b > c):
                
                #imprima las variables a,b,c
               print(a, b, c)
               #de lo contrario imprima la variable a,c,b
            else:
               print(a, c, b)
               
    #si la variable c es mayor a a va por le verdadero
    if (c > a):
    # si la variable c es mayor a b va por el verdadero
        if (c > b):
        #si la variable b es mayor a a va por el verdadero
            if(b > a):
                
                #imprima c,b,a
               print(c, b, a)
            #de lo contrario imprima c,a,b
            else:
               print(c, a, b)
               
# si la variable b es mayor a a va por el verdadero
    if (b > a):
        # si la variable b es mayor a c va por el verdadero
        if (b > c):
            # si la variable a es mayor a c va por el verdadero
            if(a > c):
                #imprima b,a,c de lo contrarion imprima b,c,a
               print(b, a, c)
            else:
               print(b, c, a)

# si la seleccion es igual y solo igual a 2
if (e == 2):
    # si a es menor a b 
    if (a < b):
        #si a es menor que c
        if (a < c):
            #si b es menor que c
            if(b < c):
                #imprima a,b,c de lo contrario imprima a,c,b
               print(a, b, c)
            else:
               print(a, c, b)
               
               
    #si c es menor que a 
    if (c < a):
        #si c es menor que b
        if (c < b):
            # si b es menor que a
            if(b < a):
                #imprima c,b,a de lo contrario imprima c,a,b
               print(c, b, a)
            else:
               print(c, a, b)
    # si b es menor que a
    if (b < a):
        # si b es menor que c
        if (b < c):
            # si a es menor que c
            if(a < c):
                
            #imprima b,a,c de lo contrario imprima b,c,a
               print(b, a, c)
            else:
               print(b, c, a)
# si a es igual y solo igual a b
if (a == b):
   # imprima que los numeros ingresados b y a son iguales
    print("b y a son iguales")
    
    # si a es igual y solo igual a c imprima a y c son iguales
    if (a == c):
        print("a y c son iguales")
        # si b es igual y solo igual a c imprima b y c son iguales
        if(b == c):
           print(" b y c con iguales")
           # si a b y c son igual y solo igual imprima a,b,c son iguales
           if(a == b == c):
              print("todos son iguales")
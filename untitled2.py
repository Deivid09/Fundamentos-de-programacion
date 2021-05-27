# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:51:52 2021

@author: trausch
"""

"Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10"
"imprimir en pantalla la leyenda Todos los números son menores a diez"

Num1 = int(input("Ingrese un Numero1: "))
Num2 = int(input("Ingrese un Numero2: "))
Num3 = int(input("Ingrese un Numero3: "))

if Num1 < 10 and Num2 < 10 and Num3 < 10 :
    print ("todos los numeros son menor a 10")
else:
    print ("uno de los numeros es mayor que 10")
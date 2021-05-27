# -*- coding: utf-8 -*-
"""Created on thu feb 15 2021
Autor Deivid
Spyder Editor
This is a temporary script file.
Descripcion:
     Realice un programa que obtenga el índice de masa corporal de
     una persona, ingresando la estatura en centímetros
     y el peso en kilos.
"""

# declaracion de variables y/o constantes


# Entrada - captura de datos


var_ent_peso = int(input("cual es su peso en Kg? : "))
 
var_ent_estatura = int(input("Cual es su estatura en Cm? :"))

conversion = (var_ent_estatura / 100)
# proceso - realizando calculos

var_imc = (var_ent_peso / conversion)




# salida - imprimiendo los resultados

print ("su IMC es :", var_imc)

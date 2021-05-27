# -*- coding: utf-8 -*-
"""Created on thu feb 15 2021
Autor Deivid
Spyder Editor
This is a temporary script file.
Descripcion:
Calcular el área y perímetro de un rectángulo.
"""
# declaracion de variables y/o constantes



# Entrada - captura de datos

var_ent_base =int(input("ingrese base de rectangulo : "))
var_ent_altura = int(input("ingrese altura de rectangulo : "))


# proceso - realizando calculos

area = (var_ent_base * var_ent_altura)
perimetro = ((2 * var_ent_base  )+(2 * var_ent_altura))

# salida - imprimiendo los resultados
print ("el area del rectangulo es = ", area)
print ("el perimetro del rectangulo es = ", perimetro)



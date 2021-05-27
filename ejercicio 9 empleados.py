# -*- coding: utf-8 -*-
"""Created on thu feb 15 2021
Autor Deivid
Spyder Editor
This is a temporary script file.
Descripcion:
    Realice un programa que resuelva lo siguiente: Si n Empleados 
    realizan una actividad en k horas, ¿cuántos empleados se necesitarán 
    para realizar la misma actividad en k1 horas?
"""

# declaracion de variables y/o constantes


# Entrada - captura de datos


var_ent_horas = int(input("ingrese horas para realizar el trabajo : "))
 
var_ent_actividad = int(input("actividad a realizar :"))

# proceso - realizando calculos

var_numeroempleados = (var_ent_horas / var_ent_actividad)




# salida - imprimiendo los resultados

print ("para estas actividades se requieren empleados :", var_numeroempleados )

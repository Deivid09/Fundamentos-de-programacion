# -*- coding: utf-8 -*-
"""Created on thu feb 15 2021
Autor Deivid
Spyder Editor
This is a temporary script file.
Descripcion:
Calcular el sueldo total a recibir de un empleado.  El usuario deberá ingresar
el número de horas trabajadas y el valor por cada hora. Considere en los 
cálculos el descuento de seguridad social y una bonificación del 2% para 
aquellos cuyo sueldo no supere los 300 dólares.
"""
# declaracion de variables y/o constantes



# Entrada - captura de datos

var_ent_valorh = float(input("ingrese valor de la hora : "))
var_ent_horasl = float(input("ingrese horas laboradas : "))


# proceso - realizando calculos

       
salario = (var_ent_horasl * var_ent_valorh)

descuentoSS = (salario / 1.08)

bono = (descuentoSS < 300 * 1.02)

if (bono = False :)
       print (bono)
       else 
       print ("su salario es : $", descuentoSS)

# salida - imprimiendo los resultados
print ("su salario es : $", descuentoSS)
print ( "su salario es : $", bono)


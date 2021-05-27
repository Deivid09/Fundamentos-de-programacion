# -*- coding: utf-8 -*-
"""   
Created on thu feb 15 2021
Autor Deivid
Spyder Editor
This is a temporary script file.
Descripcion:
  Calcular el área de un círculo y longitud de su circunferencia.
"""

# declaracion de librerias 




# declaracion de variables y/o constantes

pi=3.1416
# Entrada - captura de datos



var_ent_radio = int(input("cual es el radio del circulo?"))
 


# proceso - realizando calculos


var_string_area = (pi*var_ent_radio**2)

var_longitudcircunferencia = (2*pi*var_ent_radio)



# salida - imprimiendo los resultados
print  ("Area del circulo es: ", var_string_area )
print  ('Longitud de circunferencia es: ' , var_longitudcircunferencia)
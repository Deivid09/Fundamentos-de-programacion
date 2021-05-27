# -*- coding: utf-8 -*-
"""   
Created on thu feb 11 19:07 2021
Autor Deivid
Spyder Editor
This is a temporary script file.
Descripcion:
    inicio fundamentos de programacion
"""

# declaracion de librerias 


# declaracion de variables y/o constantes





# Entrada - captura de datos

var_ent_monto = int(input("ingrese valor de producto : " ))

var_ent_iva = int(input("ingrese % de iva : "))

iva= (var_ent_monto * var_ent_iva / 100)

descuento = (var_ent_monto * 5 /100)

# proceso - realizando calculos

var_valor_neto = ( ((var_ent_monto + iva)) - descuento)





# salida - imprimiendo los resultados
print ("El valor neto del producto es de : ", var_valor_neto)
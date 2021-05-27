# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:32:09 2021

@author: trausch
"""

# se tiene una calificacion de los alumnos de un curso de informatica correspondiente 
#a las asignaturas basic, pascal, fortan diseñar un algoritmo que calcule la media de 
#cada alumno

# Variable de entrada

var_e_nom = "***"
var_e_bas = 0.0
var_e_pas = 0.0
var_e_for = 0.0

var_p_s_conEst = 0

var_p_s_medEst = 0.0

#Leer nombre
var_e_nom = input("¿cual es el nombre de estudiante? : ")

# Ciclo While
while (var_e_nom != "***"):
    # inicio del ciclo

    var_e_bas = float(input (" ¿cual es la nota de BASIC? : "))
    var_e_for = float(input (" ¿cual es la nota de FORTRAN? : "))
    var_e_pas = float(input (" ¿cual es la nota de PASCAL? : "))
    
# Proceso que calcula la media del estudiante
    var_p_s_medEst = (var_e_bas + var_e_for + var_e_pas) / 3
    print (" la media de ",var_e_nom, "es : " ,var_p_s_medEst)
    var_e_nom =  input("¿cual es el nombre de estudiante? : ")
    var_p_s_conEst  += 1
    
    # fin del ciclo
print ("Cantidad de estudiantees : " ,var_p_s_conEst)
print ("Adios")
    
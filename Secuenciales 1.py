# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:39:03 2021

@author: trausch
"""

# Programa que calcula la nota de un estudiante


# Entradas
# pedir el nombre del estudiante y sus 3 notas de parciales
nomEst=input("Nombre estudiante : ")
notUnoEst= float(input("Parcial Uno: "))
notDosEst= float(input("Parcial Dos: "))
notTresEst= float(input("Parcial Tres: "))

#Calculos 
notDefEst = (notUnoEst+notDosEst+notTresEst)/3

#Imprimir los resultados - salidas


print ("La nota definitiva es : ", notDefEst)

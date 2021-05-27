# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:39:03 2021

@author: trausch
"""

# Programa que calcula la nota de un estudiante


# Entradas
# pedir el nombre del estudiante y sus 3 notas de parciales

canEst = int(input("Cantidad de estudiantes: "))
#Inicializar la variable que controla el ciclo
conRep=0
#variable para sumar nota definitiva de grupo
sumDefGru=0.0
#variable para calcular la noata promedio del grupo

proDefGru=0.0

while(conRep < canEst):
    #Instrucciones a repetir
    nomEst=input("Nombre estudiante : ")
    notUnoEst= float(input("Parcial Uno: "))
    notDosEst= float(input("Parcial Dos: "))
    notTresEst= float(input("Parcial Tres: "))

    #Calculos 
    notDefEst = (notUnoEst+notDosEst+notTresEst)/3
    
    #acumulo las definitivas del grupo
    sumDefGru = sumDefGru+notDefEst
    
    #Imprimir los resultados - salidas
    print (f"1. La nota definitiva es :  {notDefEst:.2f}")
    
    # Incrementar la variable que controla el ciclo
    conRep = conRep+1
    
#calcular el promedio del grupo
notProDefGru = sumDefGru/canEst

#imprimir nota promedio del grupo
print (f"2. La nota promedio es : {notProDefGru:.2f}")
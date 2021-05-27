# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:08:07 2021

@author: trausch
"""

# Practica 1 con arreglos tipo vectores

#Almacenar en un vector 5 notas de un parcial

# Declaracion el vector lista

listaNota = []
sumanota =0.0
notasgan = 0
notasper = 0
# Asignar valores a la lista

for poslista in range(5) :
    #leer desde teclado la nota
    notaest=float (input("Digite la nota: "))
    sumanota = sumanota + notaest
    #almacenamos la escalar en el arreglo
    listaNota.append(notaest)
    
    #imprimir el arreglo
print (listaNota)
print ("La suma de las notas es: ", sumanota)


if notaest >= 3.0:
    notasgan = notasgan + notaest
    print("Las notas ganadas son: ",notasgan)
    if notaest < 3:
        notasper = notasper + notaest
        print ("las notas perdidas son: ",notasper)
else:
    print ("la nota no es calificable...")
    
promnotas= sumanota / 5
print ("El promedio de las notas es: " ,promnotas)


#=========================


#listaNota2 = []

# Asignar valores a la lista

#for poslista in range(5) :
 #   #leer desde teclado la nota
  #  notaest=float (input("Digite la nota: "))
    #almacenamos la escalar en el arreglo
   # listaNota[poslista]=notaest
    
    #imprimir el arreglo
#print (listaNota2)

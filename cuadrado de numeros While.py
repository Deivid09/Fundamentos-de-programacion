# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:40:27 2021

@author: trausch
"""
#calcular el cuadrado de los primeros 100 numeros

# area de declaracion de variables
cantNum= 1

contNum= 1

sumCuad =0

# Entradas
cantNum= int (input ("Ingrese cantidad de numeros : "))

while  contNum <= cantNum :
    sumCuad = contNum + cuadNum
    cuadNum = contNum **2
    print ("El cuadrado del num",contNum ,"es : ",cuadNum)
    contNum = contNum + 1

print ("la suma de los cuadrados es : ", sumCuad)
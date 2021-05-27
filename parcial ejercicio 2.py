# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:53:24 2021

@author: trausch
"""

"Formula de Herón"

# Importar Librerias
import math

# Funcion  
def constantes(): #palabra reservada para funcion constantes
#variables constates
      x = 2 #variable "x"
      y = 3 #variable "y"
      z = 3 #variable "z"

      solucion(x,y,z) #llamado a funcion solucion

# Funcion
def solucion(x,y,z):  #palabra reservada para funcion solucion
      semi_perimetro = (x+y+z)/2 #formula del semi perimetro
      perimetro = x+y+z # formula del perimetro
      area = math.sqrt (4 * 2 * 1 * 1) # formula del area
      print("el area es: ", area ) #salida de area en pantalla
      print("**************************************") # separacion entre lineas
      print("el perimetro es: ", perimetro) #salida de perimetro
      print("**************************************") # separacion entre lineas
      print("el semiperimetro es : ", semi_perimetro) # salida de semiperimetro

constantes()
#Sebastian Cardona 82202113132
#Jorge Perez 82202115218
#Deivid Sanchez 82202113328
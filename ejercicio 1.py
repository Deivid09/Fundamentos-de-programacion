# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:43:02 2021

@author: trausch
"""

"Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad."

dia = int(input("ingrese dia"))
mes = int(input("ingrese mes"))
año = int(input("ingrese año"))

if dia ==24 and mes == 12:
    print ("la fecha es : ", dia ,"/", mes , "/" , año )
    print ("estamos en navidad")
else:
    print ("no estamos en navidad")
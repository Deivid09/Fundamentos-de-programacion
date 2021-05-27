# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:06:00 2021

@author: trausch
"""

#ejercicio34.py

def sueldomenor35 ():
    
    Num_Empleados = int(input("Cuantos empleados tiene la empresa: "))
    valor_de_hora = int(input("Ingrese valor de la hora: "))
    n=1
    nominatotal=1
    sueldototal=1
    sueldototal1=1
    
    while n <= Num_Empleados :
            nombre = input ( "Ingrese nombre del empleado: ")
            ("*******************")
            cantidad_de_horas= int(input("Ingrese cantidad de horas laboradas: "))
            n=n+1
            
            if cantidad_de_horas <= 35:
                sueldo = cantidad_de_horas*valor_de_hora
                dto_salud = (sueldo *12.5)/100
                dto_icbf= (sueldo * 4)/100
                sueldoNeto=sueldo - dto_salud - dto_icbf
                sueldototal=sueldototal+sueldoNeto
                print ("El sueldo a pagar de", nombre, "es: " ,  sueldoNeto)

            else:
                 sueldo1= (cantidad_de_horas*valor_de_hora)*1.5
                 dto_salud = (sueldo1 *12.5)/100
                 dto_icbf= (sueldo1 * 4)/100
                 sueldoNeto1=sueldo1 - dto_salud - dto_icbf
                 sueldototal1=sueldototal1+sueldoNeto1
                 print ("El sueldo a pagar de", nombre, "es: " ,  sueldoNeto1)

    nominatotal=sueldototal+sueldototal1
    print ("la nomina de la empresa cuesta $ ", nominatotal)
sueldomenor35()
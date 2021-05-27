# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 01:19:48 2021

@author: trausch
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:06:00 2021

@author: trausch
"""
#PROFE ESTO FUIMOS CAPAZ DE HACER, TENEMOS QUE MADRUGAR A TRABAJAR.

def sueldomenor35 ():
    
    Num_Empleados = int(input("Cuantos empleados tiene la empresa: "))
    valor_de_hora = int(input("Ingrese valor de la hora: "))
    n=1
    nominatotal=1
    sueldototal=1
    sueldototal1=1
    generom=0
    generof=0
    M=0
    F=0
    while n <= Num_Empleados :
            nombre = input ( "Ingrese nombre del empleado: ")
            ("*******************")
            cantidad_de_horas= int(input("Ingrese cantidad de horas laboradas: "))
            n=n+1
            
            if cantidad_de_horas <= 35:
                genero = (input ("Seleccione en mayuscula genero F o M : "))
                sueldo = cantidad_de_horas*valor_de_hora
                dto_salud = (sueldo *12.5)/100
                dto_icbf= (sueldo * 4)/100
                sueldoNeto=sueldo - dto_salud - dto_icbf
                sueldototal=sueldototal+sueldoNeto
                generom=generom + M
                generof=generof + F
                print ("El sueldo a pagar de", nombre, "es: " ,  sueldoNeto)
                print("-----------------------------------------")
                print ("El descuento por salud es de $ ",dto_salud)
                print("-----------------------------------------")
                print ("El descuento por ICBF es de $ ",dto_icbf)
                if genero =="M":
                    generom=generom+1
                else:
                    generof=generof+1
                if sueldototal >2000000 and sueldototal <=3000000:
                    ret1 = sueldoNeto *5 /100
                    print ("su salario se desconto el 5%",ret1)
                else:
                    print()
                if sueldototal >3000001 and sueldototal <=4000000:
                    ret2= sueldoNeto *7/100
                    print("se descontara de su salario el 7%", ret2)
                else:
                    print()
                if sueldototal >4000001 and sueldototal <=5000000:
                    ret3=sueldoNeto *9 /100
                    print("se descontara de su salario el 9%", ret3)
                else:
                    print()
                if sueldototal >5000001 and sueldototal <=6000000:
                    ret4=sueldoNeto *11 /100
                    print("se descontara de su salario el 11%", ret4)
                else:
                    print()
                                  
            else:
                genero = input ("Seleccione en mayuscula genero F o M : ")
                sueldo1= ((35*valor_de_hora)+((cantidad_de_horas-35) *(1.5*valor_de_hora)))
                dto_salud = (sueldo1 *12.5)/100
                dto_icbf= (sueldo1 * 4)/100
                sueldoNeto1=sueldo1 - dto_salud - dto_icbf
                sueldototal1=sueldototal1+sueldoNeto1
                generom=generom+M
                generof=generof+F
                print ("El sueldo a pagar de", nombre, "es: " ,  sueldoNeto1)
                print("-----------------------------------------")
                print ("El descuento por salud es de $ ",dto_salud)
                print("-----------------------------------------")
                print ("El descuento por ICBF es de $ ",dto_icbf)
                print("*****************************************")
                if genero =="M":
                    generom=generom+1
                else:
                    generof=generof+1
                if sueldototal1 >2000000 and sueldototal1 <=3000000:
                    ret1 = sueldoNeto1 *5 /100
                    print ("su salario se desconto el 5%",ret1)
                else:
                    print()
                if sueldototal1 >3000001 and sueldototal1 <=4000000:
                    ret2= sueldoNeto1 *7/100
                    print("se descontara de su salario el 7%", ret2)
                else:
                    print()
                if sueldototal1 >4000001 and sueldototal1 <=5000000:
                    ret3=sueldoNeto1 *9 /100
                    print("se descontara de su salario el 9%", ret3)
                else:
                    print()
                if sueldototal1 >5000001 and sueldototal1 <=6000000:
                    ret4=sueldoNeto1 *11 /100
                    print("se descontara de su salario el 11%", ret4)
                else:
                    print()
                     
    nominatotal=sueldototal+sueldototal1
    print ("la nomina de la empresa cuesta $ ", nominatotal)
    print ("La cantidad de Hombre es: ", generom)
    print ("La cantidad de Mujeres es: ", generof)
sueldomenor35()
        
# -*- coding: utf-8 -*-
"""Created on thu feb 15 2021
Autor Deivid
Spyder Editor
This is a temporary script file.
Descripcion:
Realice un programa que simule una calculadora básica,
con las operaciones: suma, resta, multiplicación, división y potencia.
"""

# declaracion de variables y/o constantes


opcion = 0


print("""
¿Qué quieres hacer?
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Potencia
       
""")
    
opcion = int (input("seleccione una opcion: "))     ;


# Entrada - captura de datos
 

# proceso - realizando calculos

if opcion == 1:
    Num1= int(input ("ingrese numero 1 : "))
    Num2= int(input ("ingrese numero 2 : "))
    suma =(Num1+Num2)
    print ("la suma de los dos numeros es: ", suma)
    
        
if opcion ==2:
    Num1= int(input ("ingrese numero 1 : "))
    Num2= int(input ("ingrese numero 2 : "))
    resta =(Num1-Num2)
    print ("La resta de los dos numeros es: ", resta)
    
if opcion == 3:
    Num1= int(input ("ingrese numero 1 : "))
    Num2= int(input ("ingrese numero 2 : "))
    multiplicar =(Num1*Num2)
    print ("la multiplicacion de los dos numeros es: ", multiplicar)
    
if opcion == 4:
    Num1= int(input ("ingrese numero 1 : "))
    Num2= int(input ("ingrese numero 2 : "))
    dividir =(Num1/Num2)
    print ("la division de los dos numeros es: ", dividir)
    
if opcion == 5:
    Num1= int(input ("ingrese numero 1 : "))
    Num2= int(input ("ingrese numero 2 : "))
    potencia= int(input("ingrese exponente : "))
    potencia1 =(Num1 ** potencia)
    potencia2 =(Num2 ** potencia)
    print ("La potencia del Num1 es : ", potencia1) 
    print ("La potencia del Num2 es : ", potencia2)

    

# salida - imprimiendo los resultados





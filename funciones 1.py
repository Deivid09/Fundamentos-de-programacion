# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:00:31 2021

@author: trausch
"""

#Leer de una venta el nimbre del articulo vendido, la cantidad del articulo y 
# el valor del articulo, nos piden calcular :
    #1- Valor a pagar neto
    #2- valor de iva conociendo que iva es del 19%
    #3- valor total a pagar.
def f_saludo ():
    print ("Hola bienvenido a Super15")
def f_despedida ():
    print (".....Adios gracias por su compra.....")
def f_valorfactura () : # encabezado de la funcion
    #desarrollo de la funcion
    

    #definicion de variables
    ve_nomPro = ""
    ve_cantPro = 0
    ve_valUniPro = 0.0
    
    cons_porIva = 0.19
    
    vps_netPag = 0.0
    vps_ivaPag = 0.0
    vps_totPag = 0.0
    
    
    #entrada de datos 
        
    ve_nomPro= input("ingrese producto de venta : ")
    
    ve_cantPro = int(input("ingrese cantidad de productos # "))
    
    ve_valUniPro = float(input("ingrese valor de producto $ "))
    
    #procesos
    vps_netPag = ve_cantPro * ve_valUniPro
    
    vps_ivaPag = vps_netPag * cons_porIva
    
    vps_totPag = vps_netPag + vps_ivaPag
    
    #salidas
    print ("el producto que va llevar es : ", ve_nomPro)
    print ("neto a pagar = $", vps_netPag)
    print ("iva a pagar = $", vps_ivaPag)
    print ("total a pagar = $", vps_totPag)
# llamado a la funcion
f_saludo()
f_valorfactura()
f_valorfactura()
f_despedida()
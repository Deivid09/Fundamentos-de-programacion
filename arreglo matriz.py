# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:55:59 2021

@author: trausch
"""


filas=int(input("Introduce # de filas : "))
columnas=int(input("Introduce # de columnas : "))


def mat ():

    matriz = []
    for i in range (filas):
        matriz.append([])
        for j in range (columnas):
            valor = int (input("fila {}, columna {} : ".format (i+1 , j+1)))
            matriz[i].append(valor)

            
        
    print ()
    for fila in matriz:
        print ("[", end=" ")
        for elemento in fila:
            print("{:2}".format(elemento), end=" ")
        print("]")
    print()
    
    sumdiapri =0
    for pos in range (filas):
        sumdiapri
        
    
   # diag = (input("Si quiere imprimir la diagonal digite '1' : "))
    
    #for (i=0 ; i<=2 ; i+1):
 #   if diag == ("1"):
  #     diagonal = matriz[0][0];[1][1]
   #    print(diagonal)
    
mat()


#def diag ():
    #mat()
    #diag = (input("Si quiere imprimir la diagonal escriba la palabra 'diagonal'"))
    #if diag == ("diagonal"):
       # diagonal = mat([0][0]) 
     #   mat [0][0]
      #  print("la diagonal es : ",diagonal)
#diag()
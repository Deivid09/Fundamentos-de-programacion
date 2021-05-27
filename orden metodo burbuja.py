# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:41:07 2021

@author: trausch
"""

#Metodos de ordeanmiento

#Crear la lista y darle valores

listaBase=[34,12,45,2,37,60,34,8]
print("LIsta base: " ,listaBase)
#Ordenar la lista con una funcion de python
listaBase.sort()
#imprimir la lista ordenada asendente
print("LIsta base Ordenada ascendente: " ,listaBase)

listaBase.sort(reverse=True)
#imprimir la lista ordenada desendente
print("LIsta base Ordenada descendente: " ,listaBase)

#=======================================
#funcion desarrollada por el programador
#ordenamiento burbuja ascendente
#print("FUNCION DESARROLLADA POR EL PROGRAMADOR - ASCENDENTE...")
def ordenamientoBurbujaAscendente (unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range (numPasada):
            if unaLista [i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i]= unaLista[i+1]
                unaLista[i+1]=temp
#=========================================================================
#print("FUNCION DESARROLLADA POR EL PROGRAMADOR - DESCENDENTE...")
def ordenamientoBurbujaDescendente (unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range (numPasada):
            if unaLista [i]<unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i]= unaLista[i+1]
                unaLista[i+1]=temp
                
unaLista = [54,26,93,17,77,31,44,55,20]
print("FUNCION DESARROLLADA POR EL PROGRAMADOR - ASCENDENTE...")
print("Lista original",unaLista)

ordenamientoBurbujaAscendente(unaLista)
print("Lista ordenada ascendente : ",unaLista)

print("============================================================")

print("FUNCION DESARROLLADA POR EL PROGRAMADOR - DESCENDENTE...")
print("Lista original",unaLista)
ordenamientoBurbujaDescendente(unaLista)
print("Lista ordenada descendente : ",unaLista)





#=================================================

def ordenamientoBurbuja (unaLista, tipo):
    if(tipo=="ascendente"):
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range (numPasada):
                if unaLista [i]>unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i]= unaLista[i+1]
                    unaLista[i+1]=temp
    if(tipo=="descendente"):
        for numPasada in range(len(unaLista)-1,0,-1):
            for i in range (numPasada):
                if unaLista [i]<unaLista[i+1]:
                    temp = unaLista[i]
                    unaLista[i]= unaLista[i+1]
                    unaLista[i+1]=temp
                    
    
    
unaLista = [54,26,93,17,77,31,44,55,20]
print("Lista original",unaLista)
tipo="ascendente"
ordenamientoBurbujaDescendente(unaLista,tipo)
print("Lista ordenada descendente : ",unaLista)
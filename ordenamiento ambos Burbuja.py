# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:48:05 2021

@author: trausch
"""
print("FUNCION DESARROLLADA POR EL PROGRAMADOR - AMBAS...")

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
     
unaLista = [54,29,93,17,77,1,44,5,20]
tipo="descendente"
print("Lista original",unaLista)
ordenamientoBurbuja(unaLista,tipo)
print("Lista ordenada de acuerdo a usuario : ",unaLista)
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 18:36:01 2021

@author: trausch
"""

#aplicacion del proceso 
# crear estructuras de datos hacer calculos y graficar esos calculos estructuras sin pandas

# ejercicio que almacena en listas - procesa en funciones
#declarar las librerias a usar  para la solucion

import matplotlib.pyplot as plt

#generar las listas con los datos inicializados

nombreProducto = ['Ron', 'Aguardiente', 'Vino', 'Cerveza', 'Tequila']
existenciaProducto = [150,110,100,200,40]




#funciones que resuelven el problema
def f_calc_tot_existencias ():
    sumaExistencias = 0
    for posLis in range (4):
        sumaExistencias = sumaExistencias + existenciaProducto[posLis]
    print ('total existencias' , sumaExistencias)    

def f_calc_tot_existencias_1 ():
    sumaExistencias = 0
    for posLis in range (4):
        sumaExistencias = sumaExistencias + existenciaProducto[posLis]
    return (sumaExistencias) 


#funcion que calcula el promedio de las existencias

def f_calc_prom_existencia ():

    promExistencias = f_calc_tot_existencias() / len(existenciaProducto)
    return(promExistencias())
    

#Llamado a las funciones que realizan  los calculos

f_calc_tot_existencias()
print ('total existencias', f_calc_tot_existencias_1())

print ('promedio de existencias = ' , f_calc_prom_existencia())

#Graficar la informacion
fig, ax = plt.subplots()
#definir el titulo del grafico
ax.set_title('Grafico de existencias de productos')
ax.set_xlabel('Productos')
ax.set_ylabel('Existencias')

#Crear el grafico

plt.bar(nombreProducto , existenciaProducto)

#publico el grafico
plt.show()
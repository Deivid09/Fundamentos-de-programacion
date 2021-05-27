# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:51:32 2021

@author: trausch
"""
#importar librerias
import pandas as pd
#Leer archivo de excel
df_archivoExcel = pd.read_excel ( 'ventas_productos_1.xlsx', index_col="Producto")
df_archivoExcel = df_archivoExcel[:10].copy()
#Imprime los archivos de excel
print(df_archivoExcel)

print (df_archivoExcel)

#imprime la grafica en vertical
df_archivoExcel.plot(kind = 'bar')

#imprime la grafica en horizontal
df_archivoExcel.plot(kind = 'barh')

#imprime la grafica en horizontal y se puede agrandar las lineas de la grafica
df_archivoExcel.plot(kind = 'barh' , width=1)

#imprime la grafica en horizontal y se puede agrandar las lineas de la grafica
df_archivoExcel.plot(kind = 'barh' , width=3)


#df_archivoExcel.plot(kind = 'bar' )

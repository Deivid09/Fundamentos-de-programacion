# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:51:32 2021

@author: trausch
"""

import pandas as pd

df_archivoExcel = pd.read_Excel ( 'ventas_productos_1.xlsx', index_col="Producto")
df_archivoExcel = df_archivoExcel[:10].copy()
print(df_archivoExcel)


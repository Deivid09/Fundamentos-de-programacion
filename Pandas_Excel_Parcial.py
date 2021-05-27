# Lectura de archivos tipo excel 
# Importar librerías
import matplotlib.pyplot as plt
import pandas as pd 

df_archivoExcel = pd.read_excel('Futbol_Partidos.xlsx')#,index_col="Producto")
#archivoExcel = pd.read_excel('Futbol_Partidos.xlsx')
n_goles_local= df_archivoExcel['goles_local']
n_goles_visita= df_archivoExcel['goles_visita']
equipo =df_archivoExcel['local']


#  Función desarrollada por el programador
# 1. Calcular Cantidad de goles de los equipos locales y graficar
def goles_local1():
    Tgoles_local = df_archivoExcel['goles_local'].sum()#  Función propia del lenguaje
    return Tgoles_local
#    def grafica1():
    fig, df = plt.subplots()
    df.set_title("Goles local")
    df.set_ylabel("Goles local")
    df.set_xlabel(" # de Goles")
    plt.barh(df_archivoExcel['local'],df_archivoExcel['goles_local'] )
    plt.show()


# 2. Calcular Cantidad de goles de los equipos visitantes y graficar
def goles_visita2():
    Tgoles_visita = df_archivoExcel['goles_visita'].sum()#  Función propia del lenguaje
    return Tgoles_visita
    fig, df = plt.subplots()
    df.set_title("Goles visitante")
    df.set_ylabel("Goles visitante")
    df.set_xlabel(" # de Goles")

    plt.barh(df_archivoExcel['visitante'],df_archivoExcel['goles_visita'])
    plt.show()

# 3. Calcular Cantidad total de goles de todos los partidos y graficar
def tot_goles3():
    total_goles_loc= df_archivoExcel['goles_local'].sum()
    total_goles_vis = df_archivoExcel['goles_visita'].sum()
    total_goles = total_goles_loc + total_goles_vis
    return total_goles
    fig, df = plt.subplots()
    df.set_title("Cantidad de goles de todos los partidos")
    df.set_ylabel("Equipo")
    df.set_xlabel(" # de Goles")

    plt.barh(["total"], total_goles)
    plt.rc('xtick', labelsize=10) 
    plt.rc('ytick', labelsize=8)
    plt.show()


# 4. Calcular Cantidad de goles de los equipos locales por campeonato y graficar    
df=pd.DataFrame(df_archivoExcel)
def goles_local_torneo():
    goles_local_torneo = df_archivoExcel.groupby(['torneo'])[['goles_local']].sum()
    return goles_local_torneo

    fig, df = plt.subplots()
    df.set_title("Goles locales por torneo")
    df.set_ylabel("torneo")
    df.set_xlabel(" # de Goles")

    plt.barh(df_archivoExcel['torneo'], df_archivoExcel['goles_local'] )
    plt.show()

# 5. Calcular Cantidad de goles de los equipos visitantes por campeonato y graficar
df=pd.DataFrame(df_archivoExcel)
def goles_visitante_torneo():
    goles_visitante_torneo = df_archivoExcel.groupby(['torneo'])[['goles_visita']].sum()
    return goles_visitante_torneo

    fig, df = plt.subplots()
    df.set_title("Goles Visitantes por torneo")
    df.set_ylabel("torneo")
    df.set_xlabel(" # de Goles")

    plt.barh(df_archivoExcel['torneo'], df_archivoExcel['goles_visita'] )
    plt.show()
# 6. Calcular Cantidad total de goles por campeonato y graficar
def tot_goles6():
    total_goles6= (df_archivoExcel.groupby(['torneo']), (df_archivoExcel['goles_local'].index+ df_archivoExcel['goles_visita'].index))
    return total_goles6
    fig, df = plt.subplots()
    df.set_title("Cantidad de goles de todos los partidos por campeonatos")
    df.set_ylabel("campeonatos")
    df.set_xlabel(" # de Goles")

    plt.barh(df_archivoExcel['torneo'], df_archivoExcel['goles_local'] + df_archivoExcel['goles_visita'])
    plt.show()




# 9. Selección que más goles realizó en todos los campeonatos
def numero_mayor():
    d_mayor=0
    for x in range (len(equipo)):
        index_d= df_archivoExcel.loc[x,'local']        
        if index_d==index_d:
            d_mayor=d_mayor+index_d
    return d_mayor





#sum_frame_by_column(awards_frame, 'torneo', ['goles_local','goles_visita'])
#sum_frame_by_column(awards_frame, 'award_sum', ['award_1','award_2','award_3'])

#def tot_goles_camp4():
#    for i in df_archivoExcel.index:
#        print("Total goles de local de "+ df_archivoExcel["local"][i]+ " en: "  +df_archivoExcel['torneo'][i]+ " es: "  +str(df_archivoExcel['goles_local'][i]) )


#dffut_prom = dfFut['goles_visita'].aggregate([np.mean,np.std])
#dffut_prom

#def torneo_area_d():

#    prom_d=area_col()/len(n_dep)
#    return prom_d

#def numero_mayor():
#    d_mayor=0
#    for x in range (len(n_dep)):
#        index_d= archivoExcel.loc[x,'Poblacion']        
#        if index_d>d_mayor:
#            d_mayor=index_d
#    return d_mayor


#def numero_menor():
#    d_menor= numero_mayor()
   
#    for m in range (len(n_dep)):        
#        index_d2= archivoExcel.loc[m,'Poblacion']
#        if index_d2<d_menor:
#            d_menor=index_d2
    
#    return d_menor


#def nombre_mayor():
#    d_mayor=0
#    for x in range (len(n_dep)):
#        index_d= archivoExcel.loc[x,'Poblacion']
#        index_n= archivoExcel.loc[x,'Departamento']        
#        if index_d>d_mayor:
#            d_mayor=index_d
#            nombre_M=index_n
            
            
   
#    return nombre_M

#def nombre_menor():
#    d_menor= numero_mayor()
   
#    for m in range (len(n_dep)):        
#        index_d2= archivoExcel.loc[m,'Poblacion']
#        index_n= archivoExcel.loc[m,'Departamento']  
#        if index_d2<d_menor:
#            d_menor=index_d2
#            nombre_m=index_n
    
#    return nombre_m

#def relacion_ha():
#    relacion=archivoExcel['Poblacion'].sum()/archivoExcel['Area'].sum()
#    return relacion

    

print("El total de goles de los locales es",(goles_local1()))
print("El total de goles de los visitantes es",(goles_visita2()))
print("El total de goles marcados en todos los partidos es ",(tot_goles3()))
print("El total de goles marcados por equipos locales en torneos son: ")
print( goles_local_torneo())
print("El total de goles marcados por equipos visitantes en torneos son: ")
print(goles_visitante_torneo())
print("El total de goles marcados en todos los partidos es ",(tot_goles6()))


print("=========================================================================")
print("la",numero_mayor())
#print("El departamento con menor poblacion es %s con %i habitantes."%(nombre_menor(),numero_menor()))

#print("En colombia hay %i habitantes por km2"%(relacion_ha()))    
#punto 1


#Punto 2


#punto 3

#punto 4


#punto 5


#pùnto 6

#plt.barh(archivoExcel['goles_local'] , [ 'local'],archivoExcel['goles_visita'] , ['visita'])
#plt.show()
#plt.pie(archivoExcel['goles_visita'],labels=archivoExcel['goles_local'])
#plt.show()

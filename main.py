import pandas as pd
from data.data1 import apartamento1,apartamento2
from helpers.crearTablasHTML import crearTabla
from helpers.crearBarras import graficarnose



tabla=pd.read_csv("./data/Siembras.csv")
barras=pd.read_csv("./data/Siembras.csv")
dataFrame= barras

campox = 'Nombre comun'
campoy = 'Arboles'
nombreGrafica = 'grafica_barras'
graficarnose(dataFrame, campox, campoy, nombreGrafica)

#EFECTUANDO FILTROS CON PYTHON

#1. DEFINIR UNA CONDICION LOGICA

#FILTRO 1
FILTRO1 = tabla.query('Ciudad == "Santa Fe de Antioquia" and Arboles > 250');


#FILTRO 2
FILTRO2 = tabla.query('Ciudad == "Caucasia"');
estadisticasCaucasia = FILTRO2.describe()


#FILTRO 3
print("FILTRO 3")
FILTRO3 = tabla.dropna(how='all').query('Vereda=="Rio Arriba" or Vereda=="La Salazar"')
print(FILTRO3)
print("<=================================================================================>")
#FILTRO4
print("FILTRO 4")
FILTRO4             = tabla.dropna(how='all').query('Vereda=="Quitasol" and Ciudad=="Bello"')
#ArbolesHectareas    = FILTRO4['Arboles', 'Hectareas'] 
print(FILTRO4)
print("<=================================================================================>")
#FILTRO5
print("FILTRO 5")
CiudadCaramanta = tabla.dropna(how='all').query('Ciudad=="Caramanta"')
FILTRO5         = CiudadCaramanta.dropna(how='all').query('Arboles>100')
print(FILTRO5)
print("<=================================================================================>")
#FILTRO6
print("FILTRO 6")
FILTRO6 = tabla.dropna(how='all').query('Ciudad=="Yarumal" and Vereda=="Mallarino"')
print(FILTRO6)
print("<=================================================================================>")

#Crear tablas

crearTabla(FILTRO1,"FILTRO1")
crearTabla(FILTRO2,"FILTRO2")
crearTabla(FILTRO3,"FILTRO3")
crearTabla(FILTRO4,"FILTRO4")
crearTabla(FILTRO5,"FILTRO5")
crearTabla(FILTRO6,"FILTRO6")


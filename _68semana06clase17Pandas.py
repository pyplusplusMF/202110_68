# Sesion del dia lunes 7 de junio

# Tema: Pandas

import pandas as pd

# Esta serie representa la población en Millones de cada país
serie = pd.Series ( [51,32,45,0.5,6.5,19.5,9.5,17,7,3.5,11.5,28.5,126,212,0.4] )
# print ('La serie es: ')
# print (serie)

lista = (serie.index)
print (lista)

# Establecemos el indice de cada fila con el nombre del país
serie.index =['Colombia', 'Perú', 'Argentina', 'Surinam', 'Nicaragua', 'Chile', 
              'Honduras', 'Guatemala', 'Paraguay', 'Uruguay', 'Bolivia', 
              'Venezuela', 'México', 'Brasil', 'Belize']
# print ('La serie es: ')
# print (serie)

# Asignamos el nombre a la columna
serie.name = 'Poblacion'
print ('La serie es: ')
print (serie)

# Acceder a un elemento de la serie mediante su indice
print ('La población de Colombia es: ', serie['Colombia'])
print ('La población de Colombia es: ', serie.Colombia)
print ('La población de Colombia y Argentina es: \n', serie[['Colombia', 'Argentina']])

print ('media ', serie.mean())
print ('mediana ', serie.median())
print ('desv estándar ', serie.std())
print ('maximo ', serie.max())
print ('minimo ', serie.min())

print (serie.describe())


dataFrame = pd.DataFrame ( {'Población': [51,32,45,0.5,6.5,19.5,9.5,17,7,3.5,11.5,
                             28.5,126,212, 0.4],
                           'Idioma':['Español', 'Español','Español','Neerlandés',
                                     'Español','Español','Español','Español',
                                     'Español','Español','Español','Español',
                                     'Español','Portugués','Inglés']
                           },
                           index = ['Colombia', 'Perú', 'Argentina', 'Surinam', 'Nicaragua', 'Chile', 
                                    'Honduras', 'Guatemala', 'Paraguay', 'Uruguay', 'Bolivia', 
                                    'Venezuela', 'México', 'Brasil', 'Belize']
                          )
print ('DataFrame a partir de una estructura tipo dict')
print (dataFrame)

# Acceder solo a la columna población
poblaciones = dataFrame ['Población']
print ('Columna poblaciones')
print (poblaciones)

# Acceder solo a la columna idioma
idiomas = dataFrame ['Idioma']
print ('Columna de idiomas')
print (idiomas)

# Mediante loc podemos extraer los elementos de una fila en concreto
datosDeMexico = dataFrame.loc['México']
datosDeColombia = dataFrame.loc['Colombia']
datosDeColombiaYBrasil = dataFrame.loc [['Colombia', 'Brasil']]

print ('Los datos de Mexico son: ')
print (datosDeMexico)

print ('Los datos de Colombia son: ')
print (datosDeColombia)

print ('Los datos de Colombia y Brasil')
print (datosDeColombiaYBrasil)
                                             # indices             # columna
poblacionDeMexicoYColombia = dataFrame.loc[['México', 'Colombia'],'Población']
print ('La poblacion de México y de Colombia son : ')
print (poblacionDeMexicoYColombia)


promedioDelDataFrame = dataFrame.mean()
print ('Promedios del dataframe')
print (promedioDelDataFrame)

informacionDelDataFrame = dataFrame.info()
print ('Informacion general del DataFrame')
print (informacionDelDataFrame)



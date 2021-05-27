'''
Se dispone de un diccionario de vinos donde las claves son nombres de vinos y los valores para cada vino 
son una lista con la información de su denominación de origen, la añada y su precio.
Diseñar una función lista_vinos (diccionario:dict, listaRango:list) -> list en que, 
dado un diccionario de vinos como el descrito y una lista con un rango de precios [menorPrecio, mayorPrecio], 
nos devuelva una lista de los nombres, ordenados alfabéticamente de los vinos 
que estén en este rango de precios.
'''


def lista_vinos (diccionario:dict, listaRango:list) -> list:
    
    listaResultado = []
    #como valor es una lista, podemos acceder a sus posiciones con un indice
    for clave, valor in diccionario.items():
        #print (clave, '-',valor[0],'-', valor[1], '-',valor[2])
        if (valor[2] >= listaRango[0] and valor[2] <= listaRango[1]):
            listaResultado.append(clave)
    listaResultado.sort()
    return listaResultado


'''
Imprimir una lista de los vinos en orden de añada
'''
def listaDeVinosXAnada (diccionario:dict) -> list:
    listaNombres = []
    listaAnada = []
    listaNombres = list (diccionario.keys())
    for clave, valor in diccionario.items():
        #listaNombres.append (clave)
        listaAnada.append (valor[1])
    
    #Algoritmo de burbuja
    for i in range (len (listaAnada)):
        for j in range (len(listaAnada)  - 1):
            if (listaAnada[j] > listaAnada[j+1]):
                
                aux = listaAnada[j]
                listaAnada[j] = listaAnada[j+1]
                listaAnada[j+1] = aux
                
                aux2 = listaNombres[j]
                listaNombres[j] = listaNombres[j+1]
                listaNombres[j+1] = aux2
    
    #print (listaNombres, listaAnada)
    listaDeListas = [[None for j in range(2)] for i in range (len(listaAnada))]
    
    for i in range (len(listaAnada)):
        listaDeListas [i][0] = listaNombres [i]
        listaDeListas [i][1] = listaAnada [i]
    
    return listaDeListas

def funcionFinal (diccionario:dict, listaRango:list) -> dict:
    diccionarioFinal = dict()
    diccionarioFinal['listaVinosRango'] = lista_vinos(diccionario, listaRango)
    diccionarioFinal['ListaOrdenadaPorAnada'] = listaDeVinosXAnada (diccionario)
    return diccionarioFinal


diccionario = {'Tinto': ['las moras',2012,49900],
               'Blanco': ['Mar de Frades',2014, 89900],
               'Rosado': ['Cavernet Saugvinon',2016,69900], 
               'Espumoso': ['Rivarose Rosado',2011,74900],
               'Tinto dulce': ['Amarone',2015, 45000], 
               'Champagne': ['Veuve Clicquot', 2016,340400]
               }
lista = [50000, 80000]

print (lista_vinos (diccionario,lista))

lista = [40000, 100000]

print (lista_vinos (diccionario,lista))
print (listaDeVinosXAnada (diccionario))

print (funcionFinal(diccionario,lista))
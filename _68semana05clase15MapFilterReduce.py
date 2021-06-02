# Clase del dia miércoles 2 de Junio 
# Tema: Lambda - Map - Filter - Reduce

def ejercicio1Map ():
    # Transformar todos los elementos de una lista a su cuadrado
    def transformarLista (lista:list) ->list:
        for i in range (len(lista)):
            lista[i] = lista[i] * lista[i]
        return lista
    lista = [1,2,4,5,3] #[1, 2, 4, 5, 3]
    print ('lista inicial = ', lista)
    lista = transformarLista (lista) #[1, 4, 16, 25, 9]
    print ('lista transformada = ', lista)
ejercicio1Map ()


def ejercicio2Map():
    # Transformar todos los elementos de una lista a su cuadrado
    def cuadrado (elemento:int) -> int:
        return elemento * elemento
    
    lista = [1,2,4,5,3] #[1, 2, 4, 5, 3]
    print ('lista inicial = ', lista)
    lista = list(map (cuadrado, lista)) #[1, 4, 16, 25, 9]
    print ('lista transformada = ', lista) 
ejercicio2Map()

def ejercicio3Map():
    # Transformar todos los elementos de una lista a su cuadrado
    # def cuadrado (elemento:int) -> int:
    #     return elemento * elemento
    
    lista = [1,2,4,5,3] #[1, 2, 4, 5, 3]
    print ('lista inicial = ', lista)
    
    funcionLambda = lambda elemento : elemento * elemento
    lista = list(map (funcionLambda, lista)) #[1, 4, 16, 25, 9]
    
    # lista = list(map (lambda elemento : elemento * elemento, lista))
    
    print ('lista transformada = ', lista)
ejercicio3Map()

def ejemploConMapYLambda ():
    #Convertir todas las temperaturas de una lista de grados Celsius a Fahrenheit
    listaTemperaturas = [12.5, 13.6, 15, 9.2]
    print ('lista de temperaturas °C = ', listaTemperaturas)
    
    listaConvertida = list (
                        map (
                            lambda gradosC: round (  (( 9/5 ) * gradosC + 32) , 2),
                            listaTemperaturas
                            )
                        )
    print ('lista convertida a °F = ', listaConvertida)
    #[54.5, 56.48, 59.0, 48.56]
ejemploConMapYLambda()


def ejercicio1Filter():
    
    # Crear una nueva tupla con los elementos que son mayores a 5
    def filtrarElementos (tupla:tuple) -> tuple:
        listaAux = []
        for elemento in tupla:
            if (elemento > 5):
                listaAux.append (elemento)
        return ( tuple (listaAux) )
    
    tupla = (210,0,15,1,2,3,4,-1,0,8) # (210, 20, 15, 1, 2, 3, 4, -1, 0, 8)
    print ('la tupla inicial es : ', tupla)
    tuplaFiltrada = filtrarElementos (tupla)
    print ('la tupla filtrada es: ', tuplaFiltrada) #(210, 20, 15, 8)

ejercicio1Filter()
    
def ejercicio2Filter():
    
    # Crear una nueva tupla con los elementos que son mayores a 5
    def filtrarElemento (elemento:int) -> bool:
        return elemento > 5   
    
    tupla = (210,0,15,1,2,3,4,-1,0,8) # (10, 20, 15, 1, 2, 3, 4, -1, 0, 8)
    tuplaFiltrada = tuple (filter (filtrarElemento, tupla))
    print ('la tupla filtrada es: ', tuplaFiltrada) # (210, 15, 8)

ejercicio2Filter()


def ejercicio3Filter ():
    # Crear una nueva tupla con los elementos que son mayores a 5
    # def filtrarElemento (elemento:int) -> bool:
    #     return elemento > 5  
    
    tupla = (210,0,15,1,2,3,4,-1,0,8) # (10, 20, 15, 1, 2, 3, 4, -1, 0, 8)
    
    tuplaFiltrada = tuple(filter ( lambda elemento : elemento > 5, tupla ))
    print ('la tupla filtrada es: ', tuplaFiltrada) #(210, 15, 8)
ejercicio3Filter()



def ejercicioFilterPares ():
    # filtrar los elementos pares de una lista
    # crear una lista nueva con todos estos elementos
    
    lista = [10,17,19,23,27,29,30,10,8,4,12,8]
    
    listaPares = list (filter ( lambda elemento: elemento % 2 == 0 , lista ))
    print ('la lista de los pares es: ', listaPares) 
    # [10, 30, 10, 8, 4, 12, 8]
    
ejercicioFilterPares()

def ejercicio1Reduce():
    # Sumar todos los elementos de una lista
    def sumatoriaLista (lista:list) -> int:
        suma = 0
        for elemento in lista:
            suma += elemento
        return suma
    
    lista = [10,17,19,23,27,29,30,10,8,4,12,8]
    suma = sumatoriaLista (lista)
    print ('suma = ', suma) # 197
ejercicio1Reduce()

def ejercicio2Reduce ():
    from functools import reduce
    
    # Sumar todos los elementos de una lista
    
    def sumatoriaElementos (sumatoria = 0, elemento = 0) ->int:
        return sumatoria + elemento
    
    lista = [10,17,19,23,27,29,30,10,8,4,12,8] 
    suma = reduce (sumatoriaElementos, lista)
    print ('suma = ', suma) # 197
ejercicio2Reduce()



def ejercicio3Reduce ():
    from functools import reduce
    
    # def sumatoriaElementos (sumatoria = 0, elemento = 0) ->int:
    #     return sumatoria + elemento
    
    # Sumar todos los elementos de una lista
    lista = [10,17,19,23,27,29,30,10,8,4,12,8] 
    
    suma = reduce (lambda sumatoria = 0, elemento = 0 : sumatoria + elemento , lista )
    print ('suma = ', suma) # 197
ejercicio3Reduce()

def ejercicioReduceConcatenacion():
    from functools import reduce
    # Concatenar una lista de strings
    
    lista = ['Java', 'PHP', 'Kotlin', 'C#', 'C++', 'Ruby']
    
    concatenacion = reduce (lambda acumuladora = '', texto = ' ': acumuladora +' '+ texto , lista)
    print (concatenacion) # Java PHP Kotlin C# C++ Ruby

ejercicioReduceConcatenacion()


def ejemploZip ():
    
    lista1 = ['a','b','c','d']
    lista2 = [10,20,30,40]
    
    lista = list (zip(lista1, lista2))
    tupla = tuple (zip (lista1, lista2))
    diccionario = dict (zip (lista1, lista2))
    
    print ('lista = ', lista) # [('a', 10), ('b', 20), ('c', 30), ('d', 40)]
    print ('tupla = ', tupla) # (('a', 10), ('b', 20), ('c', 30), ('d', 40))
    print ('diccionario = ', diccionario)
    # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
    
ejemploZip()
#clase del dia jueves 20 de mayo
def listaDeListas():
    lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    print ("lista 1: ", lista)
    print (lista[0]) #[1, 2, 3]
    
    for i in range (len(lista[0])):
        print (lista[0][i], end = " ")
        #1 2 3 
    
    for i in range (len(lista)): #ciclo externo (filas)
        for j in range (len(lista[i])): #ciclo interno (columnas)
            print (lista[i][j], end = " ")
        print ("")
    '''
    4 5 6
    7 8 9
    10 11 12
    '''
    
    lista2 = [[1,3,5,7,9],[2,4,6,8,10]]
    print ("lista 2: ", lista2)
    suma = 0 
    for i in range (len(lista2)): #ciclo externo
        suma = 0 #la variable suma se reinicia en 0
        for j in range (len(lista2[i])): #ciclo interno
            suma += lista2 [i][j] #sumatoria de cada elemento de la sublista
        print ("suma de la sublista ", i, ": ", suma)
    
            
    lista3 = [[1],[1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]
    print ("lista 3: ", lista3)
    suma = 0 
    sumaTotal = 0
    for i in range (len(lista3)): #ciclo externo
        suma = 0 #la variable suma se reinicia en 0
        for j in range (len(lista3[i])): #ciclo interno
            suma += lista3 [i][j] #sumatoria de cada elemento de la sublista
            sumaTotal += lista3[i][j]
        print ("suma de la sublista ", i, ": ", suma)    
    print ("La sumatoria total de toda la lista 3 es: ", sumaTotal)
    
    lista4 = [[1],[1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]
    print ("lista 4: ", lista4)
    n = len(lista4) # 5 elementos
    listaSumatoria = [0 for i in range (n)] # 0 0 0 0 0
    print ("listaSumatoria: ", listaSumatoria)

    for i in range (len(lista4)): #ciclo externo
        for j in range (len(lista4[i])):#ciclo interno
            listaSumatoria [i] += lista4 [i][j] #sumatoria
    print ("listaSumatoria: ", listaSumatoria)
    suma = sum(listaSumatoria) #sumar toda la lista
    print ("La suma total de la lista 4 es: ", suma)
    
    padres = [['juan','ana'], ['carlos', 'maria'], ['pedro','laura']]
    hijos  = [['marcos','alberto'], [], ['oscar']]
    
    for i in range (len(padres)): #ciclo externo... padres
        #print(padres[i])
        print ("Padre: ",padres[i][0], end = " y ")
        print ("Madre: ", padres[i][1])
        print ("Sus hijos son: ", end = " ")
        #print (hijos[i])
        for j in range (len(hijos[i])):
            print (hijos[i][j])
    
    for i in range (len(padres)):
        print ("El padre : ",padres[i][0], "tiene ", end = " ")
        print (len(hijos[i]), " hijo(s)")
    
listaDeListas()

#https://docs.python.org/es/3/library/stdtypes.html#typesseq-tuple


def tuplasConceptos():
  t1 = ('a', 'b', 'c', 'd', 'e')
  t = ('A',) + t1[1:]
  print(t)
tuplasConceptos()


def tuplasTeoria():
  txt = "but soft what light in yonder window breaks"
  palabras = txt.split()
  print (palabras)
  l = list()
  for subcadena in palabras:
      l.append((len(subcadena), subcadena))
  print(l)
  l.sort(reverse=True)
  print(l)

  res = list()

  for longitud, palabra in l:
      res.append(palabra)
      
  print(res)

  a = 4
  b = 5
  a, b = b, a
  print ("a", a)
  print ("b", b)

  addr = 'monty@python.org'
  uname, domain = addr.split('@')
  print(uname)
  print(domain)

tuplasTeoria()



#clase del dia viernes 28 de mayo
#Imprima los números del 4 al 30, de 2 en 2
def imprimirNumeros():
    
    print ('ciclo1 ')
    i = 0
    while (i <= 30):
        if (i>= 4 and i % 2 == 0):
            print (i, end = ' ')
        i += 1
    #4 6 8 10 12 14 16 18 20 22 24 26 28 30 
    print ('\nCiclo2')
    i = 4
    while (i<= 30):
        print (i, end =  ' ')
        i += 2
    #4 6 8 10 12 14 16 18 20 22 24 26 28 30
    print ('\nCiclo 3')
    start = 4
    stop = 31
    step = 2
    for i in range (start, stop, step):
        print (i, end = ' ')
    #4 6 8 10 12 14 16 18 20 22 24 26 28 30
    print ('\nCiclo 4')
    for i in range (4, 31, 2):
        print (i, end = ' ')
    #4 6 8 10 12 14 16 18 20 22 24 26 28 30
    
    
imprimirNumeros()


def imprimirNumerosLista():
    #convencional, a través de ciclos en detalle
    lista = []
    for i in range (4, 31, 2):
        lista.append(i)
    print ('lista = ', lista)
    #lista =  [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    
    #comprension de listas, todo en una sola linea
    lista2 = [i for i in range (4, 31, 2)]
    print ('lista2 = ', lista2)
    #lista2 =  [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    
    lista3 = [i for i in range (0,31,1) if (i>=4 and i%2 == 0)]
    print ('lista3 = ', lista3)
    #lista3 =  [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    
imprimirNumerosLista()

def ejercicio1():
    #Cree una lista con cuadrados de los números, de dos en dos, 
    # del 4 al 30, que son divisibles entre 3
    lista = []
    for i in range (4,31,2):
        if (i%3 == 0):
            lista.append (i**2)
    print ('lista = ', lista)
    #lista =  [36, 144, 324, 576, 900]
    
    lista2 = [i**2 for i in range (4,31,2) if (i%3 == 0) ]
    print ('lista2 = ', lista2)
    #lista2 =  [36, 144, 324, 576, 900]
ejercicio1()



def ejercicio2():
    # Cree un diccionario en el que las llaves sean una tupla entre 
    # los números del 3 al 10 y su respectivo cubo.
    # Y dónde los valores sean las listas con los cuadrados de los 
    # números de dos en dos, entre el 4 y el 30,
    # que son divisibles enteros con el primer elemento de su llave correspondiente.
    diccionario = dict()
    for i in range (3,11):
        llave = (i, i**3 )
        diccionario [llave] = []
        for j in range(4, 31, 2):
            if (j % i == 0):
                diccionario [llave].append (j ** 2)
    print (diccionario)
    
    #todo en una linea
                       #llave    #elementos     #for interno    #cond ciclo for interno    #for externo (claves)
    diccionario2 =  { (i,i**3) : [j ** 2  for j in range(4, 31, 2) if (j % i == 0) ] for i in range (3,11)  }
    print ('diccionario2 = ', diccionario2)
ejercicio2()

def ejercicio3():
    diccionario=  { (i) : [] for i in range (0,20) if (i%2 == 0)  }
    print ('diccionario = ', diccionario)
ejercicio3()





def ejercicio4 ():
    listaDelistas = [[0 for j in range (5)] for i in range (3)]
    print (listaDelistas)
    
    for i in range (3):
        for j in range (5):
            print (listaDelistas[i][j], end = ' ')
        print ('')
ejercicio4()






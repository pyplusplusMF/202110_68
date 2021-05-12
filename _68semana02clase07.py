def cadenaCaracteres():

    fruta = 'uva'
    letra1 = fruta [0] #u
    letra2 = fruta [1] #v
    letra3 = fruta [2] #a
    #letra4 = fruta [3] #IndexError 
    print(letra1, letra2, letra3)
  
    fruta = 'banana'
    tamanio = len(fruta)
    print (tamanio)

    fruta = 'banana'
    longitud = len(fruta) #6
                    #6
    #ultimo = fruta [longitud] 
                    #6 - 1 = 5
    ultimo = fruta [longitud - 1]
    print (ultimo)
    
    s = 'Monty Python'
    print(s[0:5])
    
    print(s[6:12])
    
    fruta = 'banana'
    print (fruta[:5]) 
        #0,1,2,3,4   
        
    print (fruta[3:])
    
    fruta = 'banana'
    print (fruta[3:3])
    
    fruta = 'manzana'
    print (fruta[:])   
    
    
    #saludo = '¡Hola, mundo!'
    #saludo[0] = 'J'
    
    
    saludo = '¡Hola, mundo!'
    nuevo_saludo = 'J' + saludo[1:]
    print(nuevo_saludo)
    
    print ('a' in 'banana')
    print ('hola' in 'banana')
    
    
    # 'a' = 97 en codigo ASCII
    # 'A' = 65 en codigo ASCII
    letra1 = 'a'
    letra2 = 'A'
    if (letra1 > letra2):
        print (letra1, " > ", letra2)
    elif (letra1 < letra2):
        print (letra1, "  < ", letra2)
    else:
        print (letra1, " = ", letra2)
    
    palabra = 'banana'
    index = palabra.find ('a')
    print(index)
    
    palabra = 'limon'
    index = palabra.find('z')
    print(index)
    
    palabra = 'azucar'
    print (palabra.find('uc'))
    
    frase = 'bienvenidos a la UTP y a MisionTIC'
    print (frase.find('a', 3)) #posicion 12
    print (frase.find('a', 13)) #posicion 15
    print (frase.find('a', 16)) #posicion 23
    
    camellos = 0
    vacas = 200
    print ('He visto %d camellos y %d vacas' % ( camellos, vacas) )

    cadena = "un uno, un dos, un tres"

    print (cadena.count("un"))        # Saca 4, hay 4 "un" en cadena.
    print (cadena.count("un",10))     # Saca 1, hay 1 "un" a partir de la posición 10 de cadena.
    print (cadena.count("un",0,10))   # Saca 3, hay 3 "un" entre la posición 0 y la 10.    
    cadena = "un uno, un dos, un tres"

    print (cadena.replace("un", "XXX"))        # saca por pantalla "XXX XXXo, XXX dos, XXX tres"
    print (cadena.replace("un", "XXX", 2))     # Sólo reemplaza 2 "un", así que saca por pantalla "XXX XXXo, un dos, un tres"    

    # saca "El valor es 12
    print ("El valor es {}".format(12))

    # saca "El valor es 12.3456
    print ("El valor es {}".format(12.3456))

    # Tres conjuntos {}, el primero para el primer parámetro de format(), el segundo para el segundo
    # y así sucesivamente.
    # saca "Los valores son 1, 2 y 3"
    print ("Los valores son {}, {} y {}".format(1,2,3))

    # Entre las llaves podemos poner la posición del parámetro. {2} es el tercer parámetro de format()
    # {0} es el primer parámetro de format.
    # saca "Los valores son 3, 2 y 1"
    print ("Los valores son {2}, {1} y {0}".format(1,2,3))

cadenaCaracteres()
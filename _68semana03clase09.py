#clase del dia miércoles 19 de mayo
#True break y continue
def ejemploCicloWhile():
    while True:
        numero = int(input("Ingrese un numero: "))
        if (numero % 2 == 0):
            print ("El numero es par")
            continue
        print ("El numero leido no fue par")
        seguir = int(input("Presione 1. seguir 0. Finalizar"))
        if (seguir == 1):
            continue
        else:
            break
ejemploCicloWhile()

#Range de python 
#https://docs.python.org/es/3/library/stdtypes.html#range


#ciclo for de python
#https://docs.python.org/es/3/reference/compound_stmts.html#for


def diccionariosParte1():
    datos_basicos = {
        "nombres":"Leonardo Jose",
        "apellidos":"Caballero Garcia",
        "cedula":"26938401",
        "fecha_nacimiento":"03/12/1980",
        "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
        "nacionalidad":"Venezolana",
        "estado_civil":"Soltero"
    }    
    claves = list (datos_basicos.keys())
    valores = list(datos_basicos.values())
    clavesYValores = list(datos_basicos.items())
    
    print ("claves: ", claves)
    print ("valores: ", valores)
    print ("Claves y valores: ", clavesYValores)
    
diccionariosParte1()


def diccionariosParte2():
    datos_basicos = {
        "nombres":"Leonardo Jose",
        "apellidos":"Caballero Garcia",
        "cedula":"26938401",
        "fecha_nacimiento":"03/12/1980",
        "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
        "nacionalidad":"Venezolana",
        "estado_civil":"Soltero"
    } 
    #primer ciclo, recorriendo todo el diccionario
    print ("\nPrimer Ciclo: ")
    for clave in datos_basicos:
        print ("clave: ", clave, " valor: ", datos_basicos[clave])    
        
    #segundo ciclo, recorriendo el diccionario a través de la clave
    print ("\nSegundo Ciclo: ")
    for clave in datos_basicos.keys():
        print ("clave: ", clave, " valor: ", datos_basicos[clave])
    
    #tercer ciclo, recorriendo solo los valores del diccionario
    print ("\nTercer Ciclo")
    for valor in datos_basicos.values():
        print ("Valor: ", valor)
    
    #cuarto ciclo, recorrer tanto la clave como el valor con items
    print ("\nCuarto ciclo")
    for clave, valor in datos_basicos.items():
        print ("Clave: ", clave, " valor: ", valor)
        
diccionariosParte2()

def listasPython():
  lista = [1, 2.5, 'DevCode', [5,6] ,4]

  print(lista[0]) # 1
  print(lista[1]) # 2.5
  print(lista[2]) # DevCode
  print(lista[3]) # [5,6]
  print(lista[3][0]) # 5
  print(lista[3][1]) # 6
  print('Hicimos este cambio ->',lista[1:4]) # [2.5, 'DevCode']
  print(lista[1:6]) # [2.5, 'DevCode', [5, 6], 4]
  print(lista[1:6:2]) # [2.5, [5, 6]]
  print("Hola Estructura de Lenguajes")


listasPython()
#documentacion de listas en python
#https://docs.python.org/es/3/tutorial/datastructures.html
#https://docs.python.org/es/3/tutorial/datastructures.html

def listasRelacionadas():
    preguntas = ['nombre', 'objetivo', 'sistema operativo']
    respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']

    for pregunta, respuesta in zip(preguntas, respuestas):
        print('¿Cual es tu {0}?, la respuesta es: {1}.'.format(
            pregunta, respuesta))
        
    respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']
    for i in range (len(preguntas)):
        print ("¿Cual es tu ",preguntas [i], ", la respuesta es ",respuestas[i] )
        
listasRelacionadas()
def anadirItinerario (itinerario:list):
    nombre = str(input('¿Cual es su nuevo destino?: '))
    noches = int(input('¿Cuantas noches?: '))
    listaDestino = [nombre, noches]
    itinerario.append(listaDestino)
    print ('Asi va su itinerario: ', itinerario)

def eliminarItinerario (itinerario:list):
    posicion = 0
    nombreAEliminar = str(input('¿Que destino desea eliminar? Escriba el nombre: '))
    bandera = False
    for i in range (len(itinerario)):
        if (nombreAEliminar == itinerario[i][0]):
            posicion = i
            bandera = True
            print ('Este destino será eliminado')
    if (bandera == False):
        print ('Su destino no existe aun')
    
    itinerario.pop (posicion)
    print ('Asi va su itinerario: ', itinerario)

def adicionarNoche (itinerario:list):
    nombre = str(input('¿Cual es el destino donde desea adicionar las noches?: '))
    noches = int(input('Ingrese la cantidad de noches a adicionar: '))
    bandera = False
    for i in range (len(itinerario)):
        if (nombre == itinerario[i][0]):
            itinerario[i][1] += noches
            bandera = True
            print ('Se añadieron ', noches, ' noches adicionales')
    if (bandera == False):
        print ('Su destino no existe aun')
        
    print ('Asi va su itinerario: ', itinerario)


'''itinerario[0], itinerario[-1] = itinerario[-1], itinerario[0]
print (itinerario)'''


def funcionPrincipal(itininerario:list):
    continuar = 'si'
    while continuar == 'si':
        print ('Bienvenido ...')
        print ('¿Que desea usted hacer?')
        print ('1. Ver itinerario')
        print ('2. Añadir un nuevo itinerario')
        print ('3. Eliminar itinerario')
        print ('4. Adicionar noche a un destino')
        print ('5. Salir')
        opcion = int(input('Ingrese un numero: '))
        if (opcion == 1):
            print ('Nombre\tNoches')
            for i in range (len(itininerario)):
                print (itininerario[i][0], '\t',itininerario[i][1])
        elif (opcion == 2):
            anadirItinerario (itininerario)
        elif (opcion == 3):
            eliminarItinerario (itininerario)
        elif (opcion == 4):
            adicionarNoche (itininerario)
        elif (opcion == 5):
            print ('Hasta luego!')
        
        continuar =str(input('Desea repetir todo? si/no'))
        if (continuar == 'no'):
            print ('Chao!')


#La lista contiene el nombre y la cant de dias
itinerario = [['Santa Marta',1],
            ['Cartagena',2],
            ['San Andres',4]]
print ('Itinerario Original: ', itinerario)

funcionPrincipal (itinerario)
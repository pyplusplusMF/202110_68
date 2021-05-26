def ejercicioItinerario ():
    #La lista contiene el nombre y la cant de dias
    itinerario = [['Santa Marta',1],
                ['Cartagena',2],
                ['San Andres',4]]
    print ('Itinerario Original: ', itinerario)

    nombre = str(input('¿Cual es su nuevo destino?: '))
    noches = int(input('¿Cuantas noches?: '))
    listaDestino = [nombre, noches]
    itinerario.append(listaDestino)
    print ('Asi va su itinerario: ', itinerario)

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
#ejercicioItinerario()

def preguntar():
    print ('Bienvenido ...')
    
    while True:
        ejercicioItinerario()
        continuar = str(input('Quiere realizar todo el proceso nuevamente? '))
        if (continuar == 'si'):
            continue
        else:
            break
preguntar()

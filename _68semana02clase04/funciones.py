'''
    Autor: Maria Medina
    Fecha: 6 - mayo - 2021 8:22 a.m.
    Practica de Funciones definidas por el usuario
'''
def operaciones ():
    #Entrada: se asignan valores a las variables x e y
    x = float(input("Por favor ingrese el valor de x: "))
    y = float(input("Por favor ingrese el valor de y: "))
    #Proceso: calcular las operaciones solicitadas: suma, resta, mult, div
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    #Salida: Se muestran las operaciones realizadas
    print (str(x) + " + " + str(y) + " = " + str(suma))
    print (str(x) + " - " + str(y) + " = " + str(resta))
    print (str(x) + " * " + str(y) + " = " + str(multiplicacion))
    print (str(x) + " / " + str(y) + " = " + str(division))
#operaciones()
#operaciones()
#operaciones()



def operaciones2 (x , y):
    '''
    parametros:

        x (float)
        y (float)

    salida:

        Mostrar la suma de x + y
        Mostrar la resta de x - y
        Mostrar la multiplicacion de x * y
        Mostrar la division de x / y
    '''
    #Proceso: calcular las operaciones solicitadas: suma, resta, mult, div
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    #Salida: Se muestran las operaciones realizadas
    print (str(x) + " + " + str(y) + " = " + str(suma))
    print (str(x) + " - " + str(y) + " = " + str(resta))
    print (str(x) + " * " + str(y) + " = " + str(multiplicacion))
    print (str(x) + " / " + str(y) + " = " + str(division))

#operaciones2 (20.5, 30.5)
#operaciones2 (10, 30.5)
#operaciones2 (30.8, 30.9)
#operaciones2 (11, 20)

def operacionSuma (x , y):
    '''
    parametros:

        x (float)
        y (float)
    
    retorno:

        cadena de texto mostrando la operacion suma
    '''
    x = float(x)
    y = float (y)
    suma = x + y
    retorno = str(x) + " + " + str(y) + " = " + str(suma)
    return retorno
    
def operacionResta (x:float, y:float) -> str:
    '''
    parametros:
        x (float)
        y (float)
    
    retorno:
        cadena de texto mostrando la operacion resta
    '''
    x = float(x)
    y = float (y)
    resta = x - y
    retorno = str(x) + " - " + str(y) + " = " + str(resta)
    return retorno

def saludo(cadena):
    return "Hola {}! ¿cómo estas?".format(cadena)



    
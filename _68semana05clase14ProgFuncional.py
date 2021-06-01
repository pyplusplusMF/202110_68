#Clase del dia lunes 31 de mayo
def ejemplo1():
    #Ejemplo 1
    def suma (valor1 = 0, valor2 = 0):
        return valor1 + valor2

    def operacion (funcion, valor1 = 0, valor2 = 0):
        return (funcion (valor1, valor2))

    funcionSuma = suma
    resultado = operacion (funcionSuma, 10, 20)
    print ('resultado = ', resultado)
#ejemplo1()

#Ejemplo 2
def ejemplo2():
    #funcion que crea funciones a partir de un operador de tipo caracter
    def crearFuncion(operador:str):
        if (operador == '+'):
            def suma (valor1 = 0, valor2 = 0):
                return valor1 + valor2
            return suma
        elif (operador == '-'):
            def resta (valor1 = 0, valor2 = 0):
                return valor1 - valor2
            return resta
        elif (operador == '*'):
            def multiplicacion (valor1 = 0, valor2 = 0):
                return valor1 * valor2
            return multiplicacion
        elif (operador == '/'):
            def division (valor1 = 0, valor2 = 0):
                return valor1 / valor2
            return division     

    def operacion (funcion, valor1 =0, valor2 = 0):
        return ( funcion (valor1, valor2) )

    funcionSuma = crearFuncion('+')
    funcionResta = crearFuncion('-')
    funcionMultiplicacion = crearFuncion ('*')
    funcionDivision = crearFuncion ('/')

    resultado1 = operacion (funcionSuma, 10, 20)
    print ('resultado suma = ', resultado1)

    resultado2 = operacion (funcionResta, 10, 20)
    print ('resultado resta = ', resultado2)

    resultado3 = operacion (funcionMultiplicacion, 10, 20)
    print ('resultado multiplicacion = ', resultado3)

    resultado4 = operacion (funcionDivision, 10, 20)
    print ('resultado division = ', resultado4)
ejemplo2()
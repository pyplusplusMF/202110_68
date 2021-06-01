# clase del lunes 31 de mayo
# Funciones anónimas en python. Programación Funcional
# lambda argumentos_de_la_funcion : cuerpo_de_la_funcion

def ejemplo1():
    def funcionSuma (valor1 = 0, valor2 = 0):
        return valor1 + valor2
    def operacion (funcionX, valor1 = 0, valor2 = 0):
        return (funcionX (valor1, valor2))
    resultado1 = operacion (funcionSuma, 10, 20)
    print ('resultado1 = ', resultado1)   

    #Todo en una linea...No se debe abusar de lambda.. El codigo se hará dificil de comprender
    funcionSuma = lambda valor1 = 0, valor2 = 0: valor1 + valor2
    operacion = lambda funcionX, valor1 = 0, valor2 = 0: (funcionX (valor1, valor2))
    resultado2 = operacion (funcionSuma, 10, 20)
    print ('resultado2 = ', resultado2)
ejemplo1()

def ejemplo2():
    #ejercicio con lambda
    #Funcion para el cuadrado de un numero
    def cuadrado (x):
        return x**2
    print ('funcioncuadrado = ',cuadrado(4))

    funcionCuadrado = lambda x : x * x
    print ('lambda = ', funcionCuadrado(4))
ejemplo2()

### Explicar esto nuevamente Miércoles 2 de Junio

def ejercicio2Lambda():
    #Ejercicio con lambda
    #funcion que calcula la multiplicacion de dos numeros
    def multi (x, y):
        return x * y
    print ('multi ', multi(3,4))
    
    funcionMulti = lambda x, y : x * y
    print ('lambda = ', funcionMulti(3,4))
ejercicio2Lambda()

def ejercicio3Lambda():
    #Ejercicio con lambda y condicionales
    mayor = lambda x,y: x if x > y else y
    print ( 'Mayor = ', mayor (40, 1))
    print ( 'Mayor = ', mayor (-40, 1))
ejercicio3Lambda()

def ejercicio4Lambda():
    #Ejercicio con lambda retornando un lambda
    #retorna una funcion lambda de otra funcion
    def funcion (valor):
        return lambda x : x * valor

    var1 = funcion (2) #aqui var1 llama a la funcion
    #resulta que var1 retorna el equivalente de 
    #lambda x : x * 2, 5 * 2
    var1 = var1 (5) #por eso toma el valor de 10
    print ('var1 = ',var1)
    
    var2 = funcion (3) #aqui var2 llama a la funcion
    #resulta que var2 retorna el equivalente de 
    #lambda x : x * 2, 5 * 3
    var2 = var2 (5) #por eso toma el valor de 15
    print ('var2 = ',var2)
ejercicio4Lambda()

def ejercicio5LambdaConDiccionarios():
    # Transformar los valores de un diccionario a su cuadrado
    # #ejemplo { 'a': 2...} retorna { 'a': 4}
    
    # con los ciclos de un dict
    diccionario = {'a': 1, 'b':2, 'c':3}
    print ('diccionario antes: ', diccionario)
    for clave, valor in diccionario.items():
        diccionario[clave] = valor * valor
    print ('diccionario despues: ', diccionario)
    
    print('-'*50)
    # con comprension de diccionarios
    diccionario2 = {'a': 1, 'b':2, 'c':3}
    print ('diccionario2 antes: ', diccionario2)
    diccionario2 = {clave : valor * valor
                    for clave, valor in diccionario2.items()}
    print ('diccionario2 despues: ', diccionario2)
    
    print('-'*50)
    # con lambda paso por paso
    def transformarValores (funcionLambda, diccionario):
        return {clave: funcionLambda(valor)
                for clave, valor in diccionario.items()}
    
    diccionario3 = {'a': 1, 'b':2, 'c':3}
    print ('diccionario3 antes: ', diccionario3)
    
    funcionLambda = lambda x: x * x #funcion que eleva al cuadrado
    diccionario3 = transformarValores (funcionLambda, diccionario3)
    print ('diccionario3 despues: ', diccionario3)
    
ejercicio5LambdaConDiccionarios()
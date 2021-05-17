'''
Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y
5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó
o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro
del rango permitido
'''
#diccionario = {'nota1': 0.0, 'nota2': 0.0, 'nota3':0.0}

def validacionNota ( diccionario:dict ) -> str:
    
    n1 = float(diccionario['nota1'])
    n2 = float(diccionario['nota2'])
    n3 = float(diccionario['nota3'])
    
    notaInvalida = n1 < 0.0 or n2 < 0.0 or n3 < 0.0 or n1 > 5.0 or n2 > 5.0 or n3 > 5.0 
    
    promedio = ( n1 + n2 + n3 ) / 3
    if (notaInvalida == True):
        salida = 'Invalida'
    else:
        if (promedio >= 3.0 and promedio <= 5.0):
            salida = 'Aprobó'
        elif (promedio >= 0.0 and promedio < 3.0):
            salida = 'Reprobó'

    return salida

x = {'nota1': 3.0, 'nota2': 5.0, 'nota3':1.0}
print (validacionNota(x))

x = {'nota1': 0.0, 'nota2': -1.0, 'nota3':1.0}
print (validacionNota(x))

x = {'nota1': 0.0, 'nota2': 1.0, 'nota3':0.5}
print (validacionNota(x))

x = {'nota1': 6.0, 'nota2': 5.0, 'nota3':0.5}
print (validacionNota(x))


def validacionNota2 ( diccionario:dict ) -> dict:
    
    n1 = float(diccionario['nota1'])
    n2 = float(diccionario['nota2'])
    n3 = float(diccionario['nota3'])
    diccionarioSalida = dict()
    
    notaInvalida = n1 < 0.0 or n2 < 0.0 or n3 < 0.0 or n1 > 5.0 or n2 > 5.0 or n3 > 5.0 
    
    promedio = ( n1 + n2 + n3 ) / 3
    if (notaInvalida == True):
        salida = 'Invalida'
    else:
        if (promedio >= 3.0 and promedio <= 5.0):
            salida = 'Aprobó'
        elif (promedio >= 0.0 and promedio < 3.0):
            salida = 'Reprobó'

    #Se arma el diccionario de salida, es decir el diccionario 
    #que retornara la funcion validacionNota2
    diccionarioSalida ['promedio'] = round (promedio,2)
    diccionarioSalida ['resultado'] = salida
    
    return diccionarioSalida

x = {'nota1': 3.0, 'nota2': 5.0, 'nota3':1.0}
print (validacionNota2(x))

x = {'nota1': 0.0, 'nota2': -1.0, 'nota3':1.0}
print (validacionNota2(x))

x = {'nota1': 0.0, 'nota2': 1.0, 'nota3':0.5}
print (validacionNota2(x))

x = {'nota1': 6.0, 'nota2': 5.0, 'nota3':0.5}
print (validacionNota2(x))



def validacionNota3 ( diccionario:dict ) -> dict:
    """
    parametro:
        diccionario (dict): tiene tres claves:  nota1, nota2 y nota3
        
    retorno:
        diccionario (dict): con dos claves: promedio y resultado
    """
    
    promedio = round (  ( ( sum(diccionario.values()) ) / len (diccionario.values()) ) , 2 )

    diccionarioSalida = dict()
    
    notaInvalida = diccionario['nota1'] < 0.0 or diccionario['nota2'] < 0.0 or diccionario['nota3'] < 0.0 or diccionario['nota1'] > 5.0 or diccionario['nota2'] > 5.0 or diccionario['nota3'] > 5.0 
    
    if (notaInvalida == True):
        salida = 'Invalida'
    else:
        if (promedio >= 3.0 and promedio <= 5.0):
            salida = 'Aprobó'
        elif (promedio >= 0.0 and promedio < 3.0):
            salida = 'Reprobó'

    #Se arma el diccionario de salida, es decir el diccionario 
    #que retornara la funcion validacionNota2
    diccionarioSalida ['promedio'] = round (promedio,2)
    diccionarioSalida ['resultado'] = salida
    
    return diccionarioSalida

x = {'nota1': 3.0, 'nota2': 5.0, 'nota3':1.0}
print (validacionNota3(x))

x = {'nota1': 0.0, 'nota2': -1.0, 'nota3':1.0}
print (validacionNota3(x))

x = {'nota1': 0.0, 'nota2': 1.0, 'nota3':0.5}
print (validacionNota3(x))

x = {'nota1': 6.0, 'nota2': 5.0, 'nota3':0.5}
print (validacionNota3(x))



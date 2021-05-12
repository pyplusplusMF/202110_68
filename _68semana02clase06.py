'''
Diseñe una funcion que reciba como parámetro un número real que represente la calificación 
numérica de un examen y retorne la calificación cualitativa correspondiente al número dado. 
La calificación cualitativa será una de las siguientes:
    0.0 a 2.9 Deficiente
    3.0 a 3.4 Regular
    3.5 a 3.9 Aceptable
    4.0 a 4.4 Bueno
    4.5 a 5.0 Excelente
'''

def notaCualitativa (nota:float) -> str:
    """
        Parametros:
            nota (float): calificación numérica de un examen
        Retorno
            str : calificación cualitativa
    """
    resultado = ''
    
    if (nota >= 0.0 and nota <= 2.9):
        resultado = 'Deficiente'
    else:
        if (nota >= 3.0 and nota <= 3.4):
            resultado = 'Regular'
        else:
            if (nota >= 3.5 and nota <= 3.9):
                resultado = 'Aceptable'
            else:
                if (nota >=  4.0 and nota <= 4.4):
                    resultado = 'Bueno'
                else:
                    if (nota >= 4.5 and nota <= 5.0):
                        resultado = 'Excelente'
                    else:
                        if (nota < 0.0 or nota > 5.0):
                            resultado = 'Nota Errada'
    return resultado
    #pass

def notaCualitativa2 (nota:float) -> str:
    """
        Parametros:
            nota (float): calificación numérica de un examen
        Retorno
            str : calificación cualitativa
    """   
    resultado = ''
    if (nota >= 0.0 and nota <= 2.9):
        resultado = 'Deficiente'
    elif (nota >= 3.0 and nota <= 3.4):
        resultado = 'Regular'
    elif (nota >= 3.5 and nota <= 3.9):
        resultado = 'Aceptable'
    elif (nota >=  4.0 and nota <= 4.4):
        resultado = 'Bueno'
    elif (nota >= 4.5 and nota <= 5.0):
        resultado = 'Excelente'
    elif (nota < 0.0 or nota > 5.0):
        resultado = 'Nota Errada'
    
    return resultado    



def notaCualitativa3 (nota:float) -> str:
    """
        Parametros:
            nota (float): calificación numérica de un examen
        Retorno
            str : calificación cualitativa
    """  
    resultado = ''
    categoria1 = nota >= 0.0 and nota <= 2.9 #False or True
    cateogria2 = nota >= 3.0 and nota <= 3.4 #False or True
    categoria3 = nota >= 3.5 and nota <= 3.9 #False or True
    categoria4 = nota >= 4.0 and nota <= 4.4 #False or True
    categoria5 = nota >= 4.5 and nota <= 5.0 #False or True
    categoriaInvalida = nota < 0.0 or nota > 5.0 #False or True
    
    if (cateogria2 or  categoria3 or categoria4 or categoria5):
        print ("¡Aprobado!")

    if (categoria1):
        print ("Reprobado")

    
    
    if (categoria1):
        resultado = 'Deficiente'
    elif (cateogria2):
        resultado = 'Regular'
    elif (categoria3):
        resultado = 'Aceptable'
    elif (categoria4):
        resultado = 'Bueno'
    elif (categoria5):
        resultado = 'Excelente'
    elif (categoriaInvalida):
        resultado = 'Nota Errada'   

    return resultado


print ( notaCualitativa (5.0) )

n = 4.0
print (notaCualitativa (n))

n = 1.0
print (notaCualitativa (n))

n = -1
print (notaCualitativa (n))

n = 6.0
print (notaCualitativa (n))


n = 6.0
print ("F2", notaCualitativa2 (n))

n = 1.0
print ("F3", notaCualitativa3 (n))

n = 3.5
print ("F3", notaCualitativa3 (n))






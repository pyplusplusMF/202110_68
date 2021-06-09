# Miércoles 9 de Junio
# Ejemplo de Reto 5
# Ejercicio de ejemplo anterior
# _68semana06clase17PandasEjercicio.py

def ejemploReto5 (nombreArchivo:str) -> dict:
    import pandas as pd
    dataFrame = pd.read_csv(nombreArchivo)
    # print (dataFrame)
    # dataFrame.info()
    nombres = list ( dataFrame ['name'] )
    # print (nombres)
    mayorEdad = max ( dataFrame['age'])
    # print (mayorEdad)
    menorEdad = min ( dataFrame ['age'])
    # print (menorEdad)
    tarifaPromedio =  round ( (dataFrame['fare'].mean()), 2)
    
    diccionario = dict()
    diccionario ['nombres'] = nombres
    diccionario ['edadMayor'] = mayorEdad
    diccionario ['edadMenor'] = menorEdad
    diccionario ['tarifaPromedio'] = tarifaPromedio
    
    return diccionario
    # pass

nombre = 'titanic3.csv'
print (ejemploReto5(nombre))
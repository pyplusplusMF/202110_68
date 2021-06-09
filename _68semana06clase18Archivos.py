# Clase miércoles 9 de Junio
# Tema: Archivos

def ejemplo1CSV():
    import pandas as pd
    data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
            'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
            'age': [27, 31, 36, 53, 48, 36, 40, 34],
            'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
            'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
           }
    dataFrame = pd.DataFrame (data)
    print(dataFrame)
    dataFrame.to_csv ('archivo1.csv')
    dataFrame.to_csv ('archivo2.csv', sep = ';')
ejemplo1CSV()


def ejemplo2CSV():
    # Lectura de un archivo csv
    import pandas as pd
    dataFrame = pd.read_csv ('archivo1.csv')
    print (dataFrame)
ejemplo2CSV()


def ejemplo3CSV():
    # Personalizar la cabecera
    import pandas as pd
    dataFrame = pd.read_csv('archivo1.csv',
                           skiprows = 1,
                           names = ['UID', 'Primer Nombre', 'Apellido', 'Edad', 'Venta #1', 'Venta #2'])
    print (dataFrame)
    print (dataFrame['Primer Nombre'])
ejemplo3CSV()


def ejemplo4CSV():
    import pandas as pd
    dataFrame = pd.read_csv ('archivo1.csv',
                             skiprows = 1,
                             names = ['UID', 'Primer Nombre', 'Apellido', 'Edad', 'Venta #1', 'Venta #2'],
                             na_values = ['?'],
                             index_col = 'UID'
                            )
    print (dataFrame)
ejemplo4CSV()

def ejemplo1EXCEL():
    import pandas as pd
    data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
            'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
            'age': [27, 31, 36, 53, 48, 36, 40, 34],
            'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
            'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
           }
    dataFrame = pd.DataFrame (data)
    print (dataFrame)
    dataFrame.to_excel ('archivo3.xlsx',sheet_name = 'Ejemplo 1')
# ejemplo1EXCEL()

def ejemplo2EXCEL():
    import pandas as pd
    dataFrame = pd.read_excel ('archivo3.xlsx', sheet_name = 'Ejemplo 1')
    print (dataFrame)
# ejemplo2EXCEL()


def ejemplo1TXT():
    # Escritura de un archivo TXT
    listaDatos = ['Linea #1', 'Linea #2', 'Linea #3', 'Linea #4', 'Linea #5']
    archivo = open ('archivo4.txt','w')
    for linea in listaDatos:
        archivo.write (linea)
        archivo.write ('\n')
    archivo.close ()
ejemplo1TXT()

def ejemplo2TXT():
    # Escritura de un archivo TXT
    listaDatos = ['Linea #1', 'Linea #2', 'Linea #3', 'Linea #4', 'Linea #5']
    archivo = open ('archivo5.txt','w')
    archivo.writelines ('%s\n'% s for s in listaDatos)
    archivo.close()
ejemplo2TXT()

# Lectura
def ejemplo3TXT():
    archivo = open ('archivo5.txt', 'r')
    lineas = archivo.readlines()
    print (lineas)
    lineas = [s.strip ('\n') for s in lineas]
    print (lineas)
ejemplo3TXT()


def ejemplo1JSON():
    import json

    data = {}
    data['clients'] = []

    data['clients'].append({
        'first_name': 'Sigrid',
        'last_name': 'Mannock',
        'age': 27,
        'amount': 7.17})

    data['clients'].append({
        'first_name': 'Joe',
        'last_name': 'Hinners',
        'age': 31,
        'amount': [1.90, 5.50]})

    data['clients'].append({
        'first_name': 'Theodoric',
        'last_name': 'Rivers',
        'age': 36,
        'amount': 1.11})

    with open('archivo6.json', 'w') as file:
        json.dump(data, file, indent=4)
ejemplo1JSON()


def ejemplo2JSON():
    import json
    with open ('archivo6.json') as file:
        data = json.load (file)
    print (data)
    for cliente in data['clients']:
        print ('Primer Nombre', cliente['first_name'])
        print ('Apellido', cliente['last_name'])
        print ('Edad', cliente['age'])
        print ('Monto', cliente['amount'])
ejemplo2JSON()

def ejemplo3JSON():
    import json
    import requests
    respuesta = requests.get ('http://ip-api.com/json/208.80.152.201')
    datos = json.loads(respuesta.content)
    print (datos)
ejemplo3JSON()
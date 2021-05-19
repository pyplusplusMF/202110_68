#inicio de la semana 3 - Clase 7
#Jueves 13 de Mayo


def claseDiccionarios():
    #creacion
    diccionario = {}
    print(diccionario)
    diccionario2 = dict()
    print(diccionario2)

    diccionario = {"total": 55}
    print(diccionario)
    otrodiccionario = {"copia": 123.23}
    print(otrodiccionario)

    diccionarioEjemploExcel = {
        "nombre": 5 + 2,
        "telefono": 3363692,
        "edad": 33,
        "ciudad": "Pereira"
    }

    print(diccionarioEjemploExcel)

    diccionario = dict(total=55, descuento=True, subtotal=15)
    print(diccionario)

    usuario = {
        'nombre': 'Nombre del usuario',
        'edad': 23,
        'curso': 'Curso de Python',
        'skills': {
            'programacion': True,
            'base_de_datos': False
        },
        'No medallas': 10
    }
    print(usuario)

    print(usuario['curso'])  #Curso de Python
    print(usuario['skills'])  #{'programacion': True, 'base_de_datos': False}
    print(usuario['skills']['base_de_datos'])  #False

    diccionario = dict()
    print(diccionario)

    diccionario['marca'] = 'Mazda'
    print(diccionario)
    print(diccionario['marca'])  #Mazda

    diccionario['marca'] = 'Subaru'
    print(diccionario['marca'])  #Subaru

    print(diccionario)


claseDiccionarios()


def metodosDiccionario():
    #clear()
    versiones = dict(python=2.7, zope=2.13, plone=5.1)
    print(versiones)

    versiones.clear()
    print(versiones)

    versiones = dict(python=2.7, zope=2.13, plone=5.1)
    otra_versiones = versiones.copy()
    print(versiones == otra_versiones)

    #fromkeys()

    secuencia = ('python', 'zope', 'plone')
    versiones = dict.fromkeys(secuencia)
    print("Nuevo Diccionario : %s" % str(versiones))
    print("Nuevo Diccionario : {}".format(str(versiones)))

    versiones = dict.fromkeys(secuencia, 0.1)
    print("Nuevo Diccionario : %s" % str(versiones))

    versiones = dict(python=2.7, zope=2.13, plone=5.1)
    print(versiones.get('plone'))

    versiones = dict(python=2.7, zope=2.13, plone=5.1)

    print(versiones.items())

    Estudiantes = {
        'Alumno1': {
            'nombre': 'Daniel',
            'edad': 11,
            'estatura': 1.75,
            'grado': 'Master'
        },
        'Alumno2': {
            'nombre': 'David',
            'edad': 32,
            'estatura': 1.85,
            'grado': 'Doctor'
        }
    }

    #print(Estudiantes)
    print(Estudiantes['Alumno1']['nombre'])

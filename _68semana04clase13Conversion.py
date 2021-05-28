def conversion():
    texto = 'abcdefgaaaaaaaaa'
    print ('texto = ', texto)
    
    lista = list(texto)
    print ('lista = ', lista)
    #lista =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    
    tupla = tuple (texto)
    print ('tupla = ', tupla)
    #tupla =  ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')
    
    conjunto = set (texto)
    print ('conjunto = ', conjunto)
    #conjunto =  {'b', 'e', 'a', 'd', 'c', 'f', 'g'}
conversion()


def conversionListas():
    lista = ['a','b','c','d','e','e','a','a','f']
    print ('lista = ',lista)
    
    tupla = tuple (lista)
    print ('tupla = ', tupla) #('a', 'b', 'c', 'd', 'e', 'e', 'a', 'a', 'f')
    
    texto = str(lista)
    print ('texto = ', texto) #['a', 'b', 'c', 'd', 'e', 'e', 'a', 'a', 'f']
    
    texto = ''.join(lista)
    print ('texto = ', texto)
    
    conjunto = set (lista)
    print ('conjunto = ', conjunto) #conjunto =  {'a', 'd', 'c', 'e', 'b', 'f'}
    
    
    tupla = ('a','b','c','d','e','e','a','a','f')
    lista = list (set(tupla))
    print ('lista = ', lista) #lista =  ['d', 'f', 'b', 'c', 'a', 'e']

conversionListas()
#https://docs.python.org/es/3/library/stdtypes.html#str.join




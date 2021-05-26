def teoriaConjuntos():
    s = {True, 3.14, None, False, "Hola mundo", (1, 2)}
    print ('s = ',s)
    s = { 3.14, False, 'Hoola',5.1, (1, 2),True, None, 5.10, 6.32, 'Hola2'}
    print ('s = ',s)

    s1 = set([1, 2, 3, 4])
    s2 = set(range(10))
    print('s1 = ', s1)
    print('s2 = ', s2)
    
    conjunto = set ()
    for i in range (5):
        elemento = int(input('Ingrese un elemento: '))
        conjunto.add (elemento)
    print (conjunto)
teoriaConjuntos()


def operacionesConjunto():
    A = {1,2,3,4,5,6,7,8,9,10,11,12}
    B = {1,3,7,11,13,17,19,23}
    #Union
    AUB1 = A.union (B)
    AUB2 = A | B
    print ('AUB = ', AUB1)
    print ('AUB = ', AUB2)
    #Interseccion
    AnB1 = A.intersection(B)
    AnB2 = A & B
    print ('AnB = ', AnB1)
    print ('AnB = ', AnB2)
    #Diferencia
    AdB1 = A.difference(B)
    AdB2 = A - B
    print ('A - B = ',AdB1)
    print ('A - B = ',AdB2)
    
    BdA1 = B.difference(A)
    BdA2 = B - A
    print ('B - A = ',BdA1)
    print ('B - A = ',BdA2)    
    
    #Diferencia simétrica
    AdsB1 = A.symmetric_difference(B)
    AdsB2 = A ^ B
    print ('A difSim B = ', AdsB1)
    print ('A difSim B = ', AdsB2)
    
operacionesConjunto()

def operacionesConjunto2():
    A = set([4, 3, 11, 7, 5, 2, 1, 4])
    B = set([11, 5, 9, 2, 4, 8])
    C = set([11, 5, 2, 4])
    D = set ([-1,-5,-3,-8])
    #SuperConjunto
    superconjunto = A.issuperset(B)
    print ('A superconjunto B? ', superconjunto)
    
    superconjunto = A.issuperset(C)
    print ('A superconjunto de C? ' , superconjunto)
    #SubConjunto
    subconjunto = B.issubset(A)
    print ('B subconjunto A? ', subconjunto)
    
    subconjunto = C.issubset(A)
    print ('C subconjunto de A? ',subconjunto)
    
    #Conjuntos Disjuntos
    disjuncion = A.isdisjoint(B)
    print ('A disjuncion B?', disjuncion)
    
    disjuncion = A.isdisjoint(D)
    print ('A disjuncion D ? ', disjuncion)
operacionesConjunto2()


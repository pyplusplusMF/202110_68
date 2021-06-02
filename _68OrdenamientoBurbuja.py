# Algoritmo de ordenamiento burbuja
# En este enlace se puede observar la construccion del algoritmo
# Video paso por paso https://youtu.be/P_xNb8nFgmA
# Mas información https://es.wikipedia.org/wiki/Algoritmo_de_ordenamiento

listaA = [1, 2, -9, 0, -25, 1, 3, 0, -89 ,50]
listaB = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

n = len(listaA)
print ('lista A = ', listaA)
print ('lista B = ', listaB)
# Inicio del Ordenamiento burbuja
for i in range (0,n): # Ciclo externo
    for j in range (0,n-1): # Ciclo interno
        # Comparacion entre la posición actual y la siguiente
        # Si el elemento actual es mayor que el siguiente
        # Entonces se realiza el intercambio de elementos
        if listaA[j] > listaA[j+1]: 
            # El primer intercambio es el de la lista A
            # Es la lista referente del ordenamiento.
            variableAuxiliar = listaA[j]
            listaA[j] = listaA[j+1]
            listaA[j+1] = variableAuxiliar
            
            # Como la lista B está relacionada con la
            # lista A, entonces se realiza también 
            # el intercambio de elementos de la lista.
            variableAuxiliar = listaB[j]
            listaB[j] = listaB[j+1]
            listaB[j+1] = variableAuxiliar
            
print ('\nlista A Ordenada = ', listaA)
print ('lista B Ordenada = ', listaB)
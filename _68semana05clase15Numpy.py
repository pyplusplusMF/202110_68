# clase miercoles 2 de junio

# linea de comando para instalar numpy
# py -m pip install numpy (conda) (En windows)
# https://numpy.org/install/

import numpy as np

arreglo = np.array([1,2,3])
print  (arreglo) # [1 2 3]


arreglo1D = np.array ( [1, 2, 3] )
print ('arreglo1D = ', arreglo1D) #  [1 2 3]
print ('type = ', type (arreglo1D)) # <class 'numpy.ndarray'>
print ('Ndim = ', arreglo1D.ndim) # 1
print ('shape = ', arreglo1D.shape) # shape =  (3,)
print ('Size = ', arreglo1D.size) #  3
print ('dtype = ', arreglo1D.dtype) # int32
print ('nbytes = ', arreglo1D.nbytes) #12


arreglo2D = np.array ( [ [1, 2], [3, 4], [5,6] ] )
print ('arreglo2D = \n', arreglo2D)
print ('type = ', type (arreglo2D)) #<class 'numpy.ndarray'>
print ('Ndim = ', arreglo2D.ndim) # 2
print ('shape = ', arreglo2D.shape) # (3, 2)
print ('Size = ', arreglo2D.size) # 6
print ('dtype = ', arreglo2D.dtype) # int32
print ('nbytes = ', arreglo2D.nbytes) # 24


arreglo1D = np.array([1, 2, 3], dtype=np.int)
print ('arreglo1D = ', arreglo1D) # [1 2 3]
print ('arreglo1D dType = ', arreglo1D.dtype) # int32

arreglo1D = np.array([1, 2, 3], dtype=np.float)
print ('\narreglo1D = ', arreglo1D) # [1. 2. 3.]
print ('arreglo1D dType = ', arreglo1D.dtype) # float64

arreglo1D = np.array([1, 2, 3], dtype=np.complex)
print ('\narreglo1D = ', arreglo1D) # [1.+0.j 2.+0.j 3.+0.j]
print ('arreglo1D dType = ', arreglo1D.dtype) # complex128
print ('Parte Real = ', arreglo1D.real) # [1. 2. 3.]
print ('Parte Imaginaria = ', arreglo1D.imag) # [0. 0. 0.]


lista = [1,2,3,4]
array1D = np.array (lista)
print ('array1D = ', array1D) # [1 2 3 4]
print ('ndim = ', array1D.ndim) # 1
print ('shape = ', array1D.shape) # (4, )


listaAnidada =  [[1,2],[3,4]]
array2D = np.array (listaAnidada)
#  [[1 2]
#  [3 4]]
print ('array2D = \n', array2D)
print ('ndim = ', array2D.ndim) #  2
print ('shape = ', array2D.shape) # (2, 2)


# Generar un array con valores constantes
# 1. Array de ceros

arrayDeCeros = np.zeros(  (2,3) )
print ('arrayDeCeros 2D = \n', arrayDeCeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]
print ('dtype = ',arrayDeCeros.dtype ) # float64

# Conversion al tipo de dato entero 64
arrayDeCeros = np.zeros(  (2,3) , dtype = np.int64)
print ('\narrayDeCeros 2D = \n', arrayDeCeros)
#  [[0 0 0]
#  [0 0 0]]
print ('dtype = ',arrayDeCeros.dtype ) # int64

# 2. Array de unos
arrayDeUnos = np.ones ( (4) ) 
print ('\narrayDeUnos 1D = ', arrayDeUnos)
 # [1. 1. 1. 1.]


 # Se genero un arreglo de unos multiplicado po 5.4
x1 = 5.4 * np.ones(10)
print ('x1', x1)
# x1 [5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4]
# se genero un arreglo de 10 posiciones con valor de 5.4
# full recibe dos argumentos y evita la multiplicacion
x2 = np.full(10, 5.4)
print ('x2', x2)
# x1 [5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4 5.4]

arreglo1D = np.empty(5)
arreglo1D.fill (10)
print ('arreglo1D = ', arreglo1D)

arreglo1D = np.full (5, 8.0)
print ('arreglo1D = ', arreglo1D)


# Usando arange

arreglo1D = np.arange (0.0, 10, 1)
print ('arreglo1D = ', arreglo1D)

arreglo1D = np.linspace (0, 10, 11)
print ('arreglo1D = ', arreglo1D)


x = np.array ([-1, 0 , 1])
y = np.array([-2, 0, 2])
print ('x + y = ', np.meshgrid(x + y) )

z = (x + y) ** 2
print ('z = ', z)



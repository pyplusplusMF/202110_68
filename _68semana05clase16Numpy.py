# Sesion jueves 3 de junio

import numpy as np

# 1. Matriz identidad
matriz = np.identity (4)
print ('matriz = \n',matriz)
#  [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
    
#2. Matriz sin ceros en la diagonal
matriz = np.eye(3, k=1)
print ('\n matriz = \n', matriz)
# matriz = 
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]
matriz = np.eye(3,k= -1)
print ('\n matriz = \n', matriz)
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]

#3. Matriz diagonal
matriz = np.diag(np.arange(0,20,5))
print ('\n matriz = \n', matriz)
#  matriz = 
# [[ 0  0  0  0]
#  [ 0  5  0  0]
#  [ 0  0 10  0]
#  [ 0  0  0 15]]
#
# Autor: LF Silva
# Data  : 12/10/2019
#
#  Introdução ao uso de Numpy - Manipulando arrays
import numpy as np

# criação de array
arr1 = np.array([ [3, 4, 5, 7, 10, 21],
                  [6, 8, 2, 14, 1, 71] ], dtype='float')

# alterando tamanho do array, sem mudar seus elementos
# os elementos são rearranjados e os novos elementos são assumem valores
# repetidos do array
print(arr1.shape)
arr2 = np.resize(arr1, (3, 8))
print(arr2)

# vale notar que o array original não é alterado!
print(arr1)
# se usar o método resize diretamente sobre o array, o tamanho do mesmo se
# altera e os novos elementos são assumidos como nulos
arr1.resize(3, 8)
print(arr1)

# É possível integrar mais elementos ao fim do array
arr3 = np.array([1, 2, 3, 4])
arr4 = np.append(arr3, [5, 6])
print(arr4)

# para arrays 2D, é possível especificar em qual eixo (0 - linha ou 1 - coluna)
# deseja-se colocar os elementos
arr5 = np.append(arr1, [[1], [2], [3]], axis=1)
print(arr5)

#
# Autor: LF Silva
# Data  : 11/10/2019
#
#  Introdução ao uso de Numpy - Acesso aos elementos
import numpy as np

# criação de array 1D
arr1 = np.array([3, 4, 5, 7, 10, 21], dtype='float')

# acesso aos elementos do array 1D
# por indice
print(arr1[0])
## operações de slicing - start:stop:step (o índice do stop não será incluído no
# slicing !!Cuidado!!
# por limites de intervalos - do início ao 4 elemento, p.e.
print(arr1[:4])

# do índice 3 ao 5 elemento do array !! Cuidado aqui !! O último indice
# não será incluído!!
print(arr1[3:5])

# do índice 2 ao último elemento do array !! Cuidado aqui !! O último indice
# não será incluído!!
print(arr1[2:])

# do índice 1 ao 5 elemento do array com intervalo de 2 !! Cuidado aqui !! O
# último indice não será incluído!!
print(arr1[1:5:2])

# sem especificação, assume-se o acesso a todos os elementos do array
print(arr1[:])

# criação de array 2D
arr2 = np.array([ [0.3, 0.40, 0.50, 0.70, 0.01, 2.1],
                  [0.2, 0.45, 0.55, 0.33, 0.11, 8.1],
                  [33,  0.20, 0.80, 0.5, 0.08, 0.61] ], dtype='float')

# acesso aos elementos do array 2D
# por semelhança, mas com duas dimensões
print(arr2[0][:])  # acesso com indices em dois colchetes
print(arr2[1,:])   # ou colchete único com indices separados por virgula

# imprimindo dos indices 0 a 1 (o último indice não é incluído) da linha do
# array e na coluna de indice 2 (3a coluna)
print(arr2[0:2,2])

# acessando elementos combinando múltiplos índices
# 1 - acesso à segunda linha completa; 0 - acesso à primeira linha completa
# 1 - acesso à segunda linha completa; 2 - acesso à terceira linha completa
print(arr2[ [1, 0, 1, 2] ])

# índices para acesso: [:] vai varrer todos os elementos de linhas 0->2
# [0,1], [0,0], [0,1], [0,2]
# [1,1], [1,0], [1,1], [1,2]
# [2,1], [2,0], [2,1], [2,2]
print(arr2[:,[1, 0, 1, 2] ])

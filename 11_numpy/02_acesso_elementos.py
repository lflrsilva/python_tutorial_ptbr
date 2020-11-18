#
# Autor: LF Silva
# Data  : 11/10/2019
#         18/11/2020
#
# Introdução ao uso de Numpy - Acesso aos elementos
# Material suplementar:
# Rotinas de indexação
# ver https://numpy.org/doc/stable/reference/routines.indexing.html
import numpy as np

# criação de array 1D
# Elementos sequenciais no array (em fila)
# arr1D = [el1, el2, el3, el4 ...]
print("Análise de arrays 1D")
arr1 = np.array([3, 4, 5, 7, 10, 21], dtype='float')

# acesso aos elementos do array 1D
# por indice
print(arr1[0])
# operações de slicing - start:stop:step (o índice do stop não será incluído no
# slicing !!Cuidado!!
# por limites de intervalos - do início ao 4 elemento, p.e.
print(arr1[:4])

# do índice 3 ao 5 elemento do array !! Cuidado aqui !! O último indice
# não será incluído!!
print(arr1[3:5])

# do índice 2 ao último elemento do array !!
print(arr1[2:])

# do índice 1 ao 5 elemento do array com intervalo de 2 !! Cuidado aqui !! O
# último indice não será incluído!!
print(arr1[1:5:2])

# sem especificação, assume-se o acesso a todos os elementos do array
print(arr1[:])

# criação de array 2D
# A estrutura é semelhante ao array 1D. Mas imagine que agora cada
# elemento do array 1D também é um array 1D
# Elementos sequenciais no array (em fila)
# arr2D = [el1, el2, el3, el4 ...]
#
# Escrevendo de outra forma
# arr2D = [el1,
#          el2,
#          el3,
#          el4 ...]
#
# Agora sabendo que cada elemento também é um array
# arr2D = [[el11, el12, el13 ...],
#          [el21, el22, el23 ...],
#          [el31, el32, el33 ...],
#          [el41, el42, el43 ...] ...]
#
print("Análise de arrays 2D")
arr2 = np.array([ [0.3, 0.40, 0.50, 0.70, 0.01, 2.1],
                  [0.2, 0.45, 0.55, 0.33, 0.11, 8.1],
                  [33,  0.20, 0.80, 0.5, 0.08, 0.61] ], dtype='float')
print("Impressão da matriz completa")
print(arr2)
# acesso aos elementos do array 2D
# por semelhança, mas com duas dimensões
print("Acesso às linhas da matriz usando \":\" ")
print(arr2[0][:])   # acesso com indices em dois colchetes
print(arr2[1, :])   # ou colchete único com indices separados por virgula

# imprimindo dos indices 0 a 1 (o último indice não é incluído) da linha do
# array e na coluna de indice 2 (3a coluna)
print("Realizando slice")
print(arr2[0:2, 2])

# acessando elementos combinando múltiplos índices
# 1 - acesso à segunda linha completa; 0 - acesso à primeira linha completa
# 1 - acesso à segunda linha completa; 2 - acesso à terceira linha completa
print(arr2[[1, 0, 1, 2]])

# índices para acesso: [:] vai varrer todos os elementos de linhas 0->2
# [0,1], [0,0], [0,1], [0,2]
# [1,1], [1,0], [1,1], [1,2]
# [2,1], [2,0], [2,1], [2,2]
print(arr2[:, [1, 0, 1, 2]])

# Usando rotinas de indexação
# criando array com os índices da diagonal de uma matriz quadrada (4,4)
ndi = np.diag_indices(4)
print(ndi)
# vamos criar uma matriz (4,4) - 16 elementos
mat1 = np.arange(16).reshape(4, 4)
print(mat1)
# agora vamos alterar todos os elementos da diagonal
mat1[ndi] = 100
print(mat1)

# busca de condição dentro do array
ret1 = np.where(mat1 == 100)
# retorno dos índices em que a condição é satisfeita
print(ret1)
# vamos complicar incluindo mais um elemento que satisfaz a condição
mat1[0][1] = 100
ret1 = np.where(mat1 == 100)
print(ret1)

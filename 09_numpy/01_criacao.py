#
# Autor: LF Silva
# Data  : 26/09/2019
#
#  Introdução ao uso de Numpy - Criação de arrays
import numpy as np

# Por padrão, criam-se listas em Pyhton como
lista1 = [1, 3, 5, 7, 9]

# As listas (arrays) geridas por Numpy são muito mais eficientes do que usando
# o padrão disponível em Pyhton. Nesse sentido, em sua grande maioria,
# usam-se os métodos disponíveis em Numpy. Por exemplo, se deseja somar
# um valor a todos os itens da lista1, a operação não é permitida
# diretamente.
# lista1 + 2      --> erro de sintaxe

## Criação de arrays para Numpy
# por cópia
lista2 = np.array(lista1)

# a operação de soma para os elementos do array é permitida
print(lista2 + 2)

# Arrays 1D
# Criação definindo valores e tipo de variável
# dtype = 'int' | 'float' | 'bool' | 'str' | 'object'
arr1 = np.array([3, 4, 5], dtype='float')

# É possível ser mais específico no tipo de variável alocado, com
# int8, int16, float32, float64 etc.

# propriedades dos arrays
print(f"Forma = {arr1.shape}")
print(f"No. de elementos = {arr1.size}")
print(f"Dim. do array = {arr1.ndim}")

# A forma do array (shape) retorna uma tupla com o número de elementos
# em cada dimensão.

# acesso aos elementos do array
print(arr1[0])
print(arr1[2])
#  print(arr1[6])    # erro - fora do limite
i = 1
print(arr1[i])

# Arrays 2D
# 3 linhas e 4 colunas
arr2 = np.array([[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]], dtype='float')
print(f"Forma = {arr2.shape}")
print(f"No. de elementos = {arr2.size}")
print(f"Dim. do array = {arr2.ndim}")

# Outros métodos para criar arrays

# Array com elementos nulos
a = np.zeros((2,2))
print(a)

# Array com elementos unitários
b = np.ones((1,2))
print(b)

# Array com mesmo valor em todos os elementos
c = np.full((2,2), 7)
print(c)

# Array como matriz identidade
d = np.eye(2)
print(d)

# Array com elementos aleatórios [0,1]
e = np.random.random((2,2))
print(e)

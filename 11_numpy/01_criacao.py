#
# Autor: LF Silva
# Data  : 26/09/2019
#         18/11/2020
#
#  Introdução ao uso de Numpy - Criação de arrays
#
# Lista N-dimensional e homogênea de elemento (mesmo espaço de memória
# por elemento). Elementos indexados (posição no array) usando N inteiros.
# Diferentes tipos de variáveis no array (int, double, bool etc).
#
# Mais informações:
# - https://numpy.org/doc/stable/reference/arrays.html
# - https://numpy.org/doc/stable/user/basics.types.html
# - https://numpy.org/doc/stable/reference/routines.html
#
# 1 - Usar numpy.matrix ou 2D numpy.ndarray?
#
# Apesar de possuir algumas operações bem convenientes para matrizes, não se
# recomenda adotar np.matrix. Por compatibilidade com outros módulos, é
# interessante usar np.array 2D. Tudo que pode ser feito com np.matrix também
# é possível com np.array. Na verdade, são mais coisas que podem ser feitas
# com np.ndarray.
#
# 2 - Operações de álgebra linear usando métodos de Numpy ou Scipy?
#
# Em outras palavras, numpy.linalg vs scipy.linalg? Os métodos de álgebra
# linear de Scipy tem todas as funcionalidades do Numpy. Além disso,
# a instalação de Scipy usa bibliotecas compiladas sempre enquanto que
# em Numpy isso é opcional. Portanto, é garantida a eficiência das
# operações ao usar Scipy.
#
# Um pequeno exemplo:
#
# >>> import numpy as np
# >>> from scipy import linalg
# >>> A = np.mat('[1 2;3 4]')
# >>> A.I   # obtém a inversa da matriz
# >>> B = np.array([[1,2],[3,4]])
# >>> linalg.inv(B)  # obtém a inversa
#
# 3 - Rotinas de Numpy
#
# Contempla:
#   - funções matemáticas (trigonemétricas, hiperbólicas,
#     exponencial etc)
#   - funções lógicas (avaliação dos elementos do array)
#   - funções I/O (entrada e saída de dados)
#   - funções de seleção, busca e contagem

import numpy as np

# Por padrão, criam-se listas em Pyhton como
lista1 = [1, 3, 5, 7, 9]

# As listas (arrays) geridas por Numpy são muito mais eficientes do
# que usando o padrão disponível em Pyhton. Nesse sentido, em sua grande
# maioria, usam-se os métodos disponíveis em Numpy. Por exemplo, se deseja
# somar um valor a todos os itens da lista1, a operação não é permitida
# diretamente.
# lista1 + 2      --> erro de sintaxe

# Criação de arrays para Numpy
# por cópia
lista2 = np.array(lista1)

# a operação de soma para os elementos do array é permitida
print(lista2 + 2)

# Arrays 1D
# Elementos sequenciais no array (em fila)
# arr1D = [el1, el2, el3, el4 ...]
#
# Criação definindo valores e tipo de variável
# dtype = 'int' | 'float' | 'bool' | 'str' | 'object'
arr1 = np.array([3, 4, 5], dtype='float')

# É possível ser mais específico no tipo de variável alocado, com
# int8, int16, float32, float64 etc.
# ver: https://numpy.org/doc/stable/user/basics.types.html

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

# 3 linhas e 4 colunas
arr2 = np.array([[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]], dtype='float')
print(f"Forma = {arr2.shape}")
print(f"No. de elementos = {arr2.size}")
print(f"Dim. do array = {arr2.ndim}")

# Outros métodos para criar arrays
# ver: https://numpy.org/doc/stable/reference/routines.array-creation.html
# Array com elementos nulos
a = np.zeros((2, 2))
print(a)

# Array com elementos unitários
b = np.ones((1, 2))
print(b)

# Array com mesmo valor em todos os elementos
c = np.full((2, 2), 7)
print(c)

# Array como matriz identidade
d = np.eye(2)
print(d)

# Array com elementos aleatórios [0,1]
e = np.random.random((2, 2))
print(e)

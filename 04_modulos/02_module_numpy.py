#
# Autor : LF Silva
# Data  : 01/05/2018
#
# Usando módulo Numpy

import numpy as np

# O principal objetivo do módulo NumPy é o tratamento de arrays (listas)
# homogêneas (de apenas um tipo de variável) e multidimensionais (vetores,
# matrizes etc). O array é tratado como uma tabela de elementos (usualmente
# números), todos do mesmo tipo, indexados por uma tupla de inteiros positivos.
# Em NumPy, as dimensões são chamadas de eixos.

# Comando para criar arrays
a = np.array( [1, 2, 3, 4] )
print("a = ", a)
# Podemos acessar os elementos como se fosse uma lista
print(a[0], a[2])
a[1] = 8
print("a novo = ", a)

# Outras propriedades do array também podem ser obtidas
print(a.ndim)    # dimensão do array
print(a.size)    # no. de elementos no array
print(type(a))   # tipo de variável no array

# Podemos criar um array de zeros e especificar o tipo de variável
b = np.zeros(10, dtype=np.float64)
print("b = ", b)

# Ou de unitários
c = np.ones(10)
print("c = ", c)

# Ainda podemos montar um array cujos elementos são igualmente espaçados
# entre si.
d = np.linspace(0.0, 1.0, 11)     # start = 0.0, end = 1.0,
                                  # number of intervals = 11
print("d = ", d)

# Por fim, podemos criar um array, definindo o espaçamento entre os pontos
e = np.arange(0.0, 1.0, 0.1)      # start = 0.0, end = 1.0,
                                  # intervals value = 0.1
print("e = ", e)

# Com arange, não é possível prever o número de elementos final devido ao
# acúmulo de erros de ponto flutuante. Portanto, linspace é mais indicado.

## Operações matemáticas
print("(b + 2c)**3 = ", (b + 2*c)**3)
b = b + 1.5
print("b*e = ", b*e)

# A maioria das funções matemáticas do modulo math estão disponíveis no NumPy
print("sin(e) = ", np.sin(e))

# O NumPy possui vários outros atributos e possibilidades. Para uma visão
# mais ampla, verifique a documentação em:
#
# https://docs.scipy.org/doc/numpy/user/quickstart.html


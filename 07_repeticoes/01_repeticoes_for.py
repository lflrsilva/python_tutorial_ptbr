#
# Autor: LF Silva
# Data : 02/06/2018
#
#  Laços e repetições em Python
#
#  Sintaxe basica:
#
#  for (it in list):
#  TAB    statement1;
#  TAB    statement2;
#         ...
#
#  Nesta sintaxe, a variável 'it' assume os valores dos elementos em 'list'
#  de modo sequencial. Por exemplo, se 'list' possui 3 elementos, 'it'
#  assume o valor do primeiro elemento ao executar os comandos dentro do
#  for pela primeira vez. Na segunda vez, 'it' assume o segundo elemento de
#  'list' e repete-se os comandos dentro do for. O procedimento se repete
#   até o último elemento de 'list' ser usado.
#
#  É possível definir o número de repetições desejado com a função
#  range([start,] stop [,step]), onde
#
#  - start : número inicial na sequência (inteiro)
#  - stop  : número final na sequência (inteiro)
#  - step  : differença entre números (inteiro)
#
#  A inclusão de start e step são opcionais. Se apenas stop é fornecido,
#  python cria uma lista iniciada em 0 até stop-1. Ou seja, é possível
#  varrer todos os elementos de uma lista usando a variável de iteração.

import numpy as np
import matplotlib.pyplot as plt

w = ['laranja', 'banana', 'pera', 'jiló']

for fruta in w:
    print(f"As frutas são {fruta:s}.")

    if(fruta == "jiló"):
        print("Desde quando jiló é uma fruta?")

# evolução de concentração
ca0 = 1.0
k   = 0.5

# variáveis numéricas
t0 = 0.0
tf = 10.0
npoints = 100

# criando array para variável temporal
t = np.linspace(t0, tf, npoints)
# reservando o espaço na memória para o array
c = np.empty(npoints)

for i in range(npoints):
    c[i] = ca0*np.exp(-k*t[i])

plt.plot(t, c)
plt.xlabel("t (s)")
plt.ylabel("c (mol/m**3)")

plt.show()

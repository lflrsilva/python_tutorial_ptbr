#
# Autor: LF Silva
# Data : 02/06/2018
#
#  Funções em Python
#
#  Sintaxe basica:
#
#  def nome_funcao (arg1, arg2, ...):
#  TAB    statement1;
#  TAB    statement2;
#         ...
#         return res
#
#  Nesta sintaxe, define-se uma função chamada 'nome_funcao' que recebe as
#  variáveis 'arg1', 'arg2', etc como argumentos. Nesse sentido, os
#  argumentos podem ser usados para realizar cálculos e retornar algum
#  resultado.
#
#  Assim, o objetivo da função é encapsular cálculos e, no código principal,
#  apenas fornecer os argumentos e obter o resultado final destes cálculos.
#
#  x = nome_funcao(a1, b2)
#
#  Seguindo a nomenclatura, a variável 'x' vai receber o valor de 'res'.

import math as m
import numpy as np
import matplotlib.pyplot as plt

def hello_me(name):
    """Função aplicada para de dar oi.

    :name: seu nome
    :returns: nada

    """
    print("Olá, %s" % name)
    return

def soma(a, b):
    return(a + b)

def microbial_growth(c0, A, b, n, t):
    """ Crescimento microbiano em lei de potência
    Ref.: Longhi et al. "Microbial growth models: A general mathematical
          approach to obtain mu_max and lambda parameters from sigmoidal
          empirical prymary models", BJChE, v. 34, N. 02, pp. 369-375, 2017
    :c0:conc. inicial
    :A: parametro
    :b: parametro
    :n: cte exponencial
    :t: tempo, h
    """
    c = c0 + np.divide(A*np.power(t, n), b + np.power(t, n) )
    return c

# função Oi
hello_me("LF")

# função soma
x = soma(5, 3)
print(x)

## Modelo de crescimento
c0 = 0.01
Aa = 2.09
bb = 9550.0
nn = 2.65

# Parametros numéricos
nt = 100
t0 = 0.0
tf = 480.0
t = np.linspace(t0, tf, nt)
c = microbial_growth(c0, Aa, bb, nn, t)

plt.plot(t, c)
plt.xlabel("t (h)")
plt.ylabel("c (n/m**3) ")
plt.show()

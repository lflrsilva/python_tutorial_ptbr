#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Teste de minimização usando programação linear
# f(x) = SUM_j  a_j * x_j
# restrições
#  SUM_j b_ij * x_j <= c_ij  para i = no. de eqs de restrição de desigualdade
#  SUM_j d_ij * x_j = e_ij   para i = no. de eqs de restrição de igualdade
#  l_i <= x_i <= u_i         para i = no. de restrições de desigualdade

# Analise do problema:
# f(x) = -x_0 + 4*x_1
# com restrições:
# -3*x_0 + x_1 <= 6
# -x_0 - 2*x_1 >= -4  (cuidado! temos que inverter os sinais!!)
# x_1 >=-3
#
# Resposta: x_0 = 10.0, x_1 = -3.0

if __name__ == "__main__":

    # definindo os coeficientes da funcao de minimizacao
    a = np.array([-1.0, 4.0])

    # definindo de forma matricial os coeficientes de desigualdade
    b = np.array([ [-3.0, 1.0], [1.0, 2.0]])
    # e limites de desigualdade
    c = np.array([6.0, 4.0])

    # definindo os limites (tuplas!)
    x0_bds = (None, None)
    x1_bds = (-3.0, None)

    res = linprog(a, A_ub=b, b_ub=c, bounds=[x0_bds, x1_bds])
    print(res)

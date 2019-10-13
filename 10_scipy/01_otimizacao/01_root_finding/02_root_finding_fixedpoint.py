#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import fixed_point

# f(x) = x + 2 cos(x) = 0
# Para metodo do ponto fixo (subst. sucessiva)
# x = g(x) = - 2 cos(x)
def func1(x):
    return - 2 * np.cos(x)

if __name__ == "__main__":
# Solucao do primeiro problema
# estimativa inicial
    xguess  = 0.3
    xsol = fixed_point(func1, xguess)
    print(f"x = {xsol:5.5e}")
    print(f"f = {xsol - func1(xsol):5.5e}")

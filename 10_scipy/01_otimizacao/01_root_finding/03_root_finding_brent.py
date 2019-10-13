#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import brentq

# Para metodo da bisecao
# f(x) = x + 2 cos(x) = 0
def func1(x):
    return x + 2 * np.cos(x)

if __name__ == "__main__":
# Solucao do primeiro problema
# estimativas iniciais
    xl  = -1.5
    xr  =  1.5
# tolerancia para metodo
    tol = 1.0e-7

    xsol = brentq(func1, xl, xr, xtol=tol)
    print(f"x = {xsol:5.5e}")
    print(f"f = {func1(xsol):5.5e}")

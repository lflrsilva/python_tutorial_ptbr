#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import root

# f(x) = x + 2 cos(x) = 0
def func1(x):
    return x + 2 * np.cos(x)

if __name__ == "__main__":
# Solucao do primeiro problema
# estimativa inicial
    xguess  = 0.3
    sol1 = root(func1, xguess)
    print(f"x = {sol1.x[0]:5.5e}")
    print(f"f = {sol1.fun[0]:5.5e}")


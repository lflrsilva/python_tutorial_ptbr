#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt


def func1(x, *args):
    p1 = args[0]
    p4 = args[1]
    T1 = args[2]
    R  = args[3]
    g  = args[4]

    gm = g/(g  -1.0)
    return gm*R*T1*((x[0]/p1)**gm + (x[1]/x[0])**gm + (p4/x[1])**gm - 3.0)

# inicio do programa
if(__name__ == "__main__"):
    # variaveis de processo
    p1 = 100.0e3    # Pa
    p4 = 1000.0e3   # Pa
    T1 = 300.0      # K
    R  = 8.31446    # J/mol K
    g  = 1.4        # cp/cv (-)

    # passagem de argumentos
    fargs = (p1, p4, T1, R, g)

    # estimativa inicial
    x0   = np.array([450e3, 700e3])

    # minimizacao usando Simplex
    res = minimize(func1, x0, args=fargs, method='Nelder-Mead',
                   options={'disp' : True})
    print("p2 = %5.5e" % (res.x[0]))
    print("p3 = %5.5e" % (res.x[1]))
    print("f = %5.5e" % (res.fun))


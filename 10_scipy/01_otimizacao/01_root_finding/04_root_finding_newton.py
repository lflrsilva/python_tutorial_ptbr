#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import newton

# Para metodo de newton ou secante ou Halley
# f(x) = x + 2 cos(x) = 0
def func1(x):
    return x + 2 * np.cos(x)

# f'(x) = -2 sin(x)
def dfunc1(x):
    return 1 - 2 * np.sin(x)

# f''(x) = -2 cos(x)
def ddfunc1(x):
    return -2 * np.cos(x)

if __name__ == "__main__":
# estimativa inicial
    xguess  = -0.3

# Se nao fornecer a funcao com a derivada da funcao, Scipy ira usar
# o metodo da secante
    xsol = newton(func1, xguess)
    print(f"Usando metodo da secante")
    print(f"x = {xsol:5.5e}")
    print(f"f = {func1(xsol):5.5e}\n")

# fornecendo a funcao da derivada, Scipy usa o metodo de newton
    xsol = newton(func1, xguess, fprime=dfunc1)
    print("Usando metodo de newton")
    print(f"x = {xsol:5.5e}")
    print(f"f = {func1(xsol):5.5e}\n")

# fornecendo as funcoes das primeira e segunda derivadas, Scipy usa
# o metodo de Halley
    xsol = newton(func1, xguess, fprime=dfunc1, fprime2=ddfunc1)
    print("Usando metodo de Halley")
    print(f"x = {xsol:5.5e}")
    print(f"f = {func1(xsol):5.5e}\n")


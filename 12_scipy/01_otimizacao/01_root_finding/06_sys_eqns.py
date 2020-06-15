#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import root

# Funcoes a resolver
# f1(x,y) = x cos(y) - 4 = 0
# f2(x,y) = x y - y - 5 = 0
def func1(x):
    return np.array(
             [ x[0] * np.cos(x[1]) - 4,
               x[1]*x[0] - x[1] - 5 ]
           )

# Jacobiano das funcoes (matrix de derivadas parciais)
def df(x):
    return np.array(
               [ [np.cos(x[1]), -x[0] * np.sin(x[1])],
                 [x[1]        ,  x[0] - 1] ]
           )

if __name__ == "__main__":
# Solucao do segundo problema
# estimativa inicial
    xguess = np.array([1.0, 1.0])

#
# DIFERENTES METODOLOGIAS COMENTADAS PARA QUE POSSAM TESTAR CADA UMA
# INDIVIDUALMENTE! VERIFIQUEM O RESIDUO DA FUNCAO OBTIDO PELOS METODOS.
# METODOS QUE USAM JACOBIANO TEM MELHOR COMPORTAMENTO, MAS MAIOR ESFORCO
# DE IMPLEMENTACAO (CALCULO DAS DERIVADAS ANALITICAS)!
#
# metodos que nao usam jacobiano (convergencia pior e maior residuo)
#  xsol   = root(func1, xguess, method='broyden1')
#  xsol   = root(func1, xguess, method='broyden2')
#  xsol   = root(func1, xguess, method='anderson')
#  xsol   = root(func1, xguess, method='krylov')
    xsol   = root(func1, xguess, method='hybr')

# metodo que usa jacobiano (melhor convergencia e menor residuo)
#  xsol   = root(func1, xguess, jac=df, method='lm')

# mostrando solucao
    for i in range(len(xsol.x)):
        print(f"x[{i:d}] = {xsol.x[i]:5.5e}")

# mostrando um residuo ponderado para as funcoes
    fres = np.sqrt(np.sum(func1(xsol.x)*func1(xsol.x)))/len(xsol.x)
    print(f"res = {fres:5.5e}")

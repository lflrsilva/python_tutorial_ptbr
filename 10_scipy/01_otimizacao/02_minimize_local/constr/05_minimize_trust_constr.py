#
# Autor: Luiz Fernando Lopes R. Silva
# Data : 10/10/2019
#

import numpy as np
from scipy.optimize import minimize, Bounds, BFGS, LinearConstraint, NonlinearConstraint

# Teste de minimização com múltiplas restrições
# min f(x_0, x_1) = 100.0*(x_1 - x_0*x_0)**2 + (1 - x_0)**2
# com restrições
# x_0 + 2*x_1  <= 1.0
# x_0**2 + x_1 <= 1.0
# x_0**2 - x_1 <= 1.0
# 2*x_0 + x_1 = 1.0
# e limites
# 0.0  <= x_0 <= 1.0
# -0.5 <= x_1 <= 2.0
#
# Resposta: x_0 = 0.4149, x_1 = 0.1701

# função objetivo
def fa(x):
    return(100*(x[1]-x[0]**2)**2 + (1.0-x[0])**2)

# jacobiano da função objetivo
def Jfa(x):
    return( [-400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0]), 200*(x[1]-x[0]**2)])

# restrições não lineares
def nl_cons(x):
    return([x[0]**2 + x[1], x[0]**2 - x[1]])

# jacobiano para restrições não lineares
def nl_Jcons(x):
    return [[2*x[0], 1], [2*x[0], -1]]

# combinação linear da hessiana para restrições não lineares
#  def nl_Hcons(x,v):
#      return v[0]*np.array([[2, 0], [0, 0]]) + v[1]*np.array([[2, 0], [0, 0]])

if __name__ == "__main__":

    # definindo limites para otimização
    lbnd = [0.0,  -0.5]   # inferior
    ubnd = [1.0, 2.0]     # superior
    bnds = Bounds(lbnd, ubnd)

    # definindo restrições lineares
    # x_0 + 2*x_1 <= 1.0
    # 2*x_0 + x_1 = 1.0
    lin_cons = LinearConstraint([[1.0, 2.0], [2.0, 1.0]],
                                [-np.inf, 1.0], [1.0, 1.0])

    # definindo restrições não-lineares
    # x_0**2 + x_1 <= 1.0
    # x_0**2 - x_1 <= 1.0
    # argumentos: função, limites, jacobiana e hessiana (usando aproximação
    # numérica - BFGS ou SR1 - ver documentação).
    nlin_cons = NonlinearConstraint(nl_cons, -np.inf, 1.0, jac=nl_Jcons,
                                    hess=BFGS())
    #  nlin_cons = NonlinearConstraint(nl_cons, -np.inf, 1.0, jac='2-point',
    #                                  hess=BFGS())

    # minimizacao usando trust-constr com aproximações de jacobiano e hessiana
    # da função objetivo
    x0 = np.array([0.5, 0.0])
    res = minimize(fa, x0, method='trust-constr', jac=Jfa, hess='2-point',
                   constraints=[lin_cons, nlin_cons],bounds=bnds,
                   options={'disp' : True})
    print("x_0 = %5.5e" % (res.x[0]))
    print("x_1 = %5.5e" % (res.x[1]))
    print("f = %5.5e" % (res.fun))
    #  print(res)

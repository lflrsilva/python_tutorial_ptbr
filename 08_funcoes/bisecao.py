#
# Autor : LF Silva
# Data  : 04/06/2018
#
# Método da biseção
from math import fabs

def solve_bisecao(func, xl, xr, tol):
    '''Busca de raiz de função contínua onde f(xl) e f(xr)
    possuem sinais opostos'''

    if (func(xl)*func(xr) > 0.0 ):
        raise Exception('Sinais iguais - biseção não é possível')

    maxit = 100
    for i in range(maxit):

        # calculo pto médio
        xm = 0.5*(xl + xr)

        # verificando convergencia
        if(fabs(func(xm)) < tol ):
            break

        if (func(xl)*func(xm) > 0.0):
            xl = xm
        else:
            xr = xm

    if(i == maxit):
        raise Exception('Não foi atingida convergência')

    return xm


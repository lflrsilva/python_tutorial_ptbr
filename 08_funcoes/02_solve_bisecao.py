#
# Autor: LF Silva
# Data : 02/06/2018
#

# módulo bisecao identificado pelo nome do arquivo (mesmo diretório!).
from bisecao import solve_bisecao

def f(x):
    return(x**2 - 3.0)

x = solve_bisecao(f, 0.0, 3.0, 1.e-7)
print("Solucão -> x = %5.5e" % x)


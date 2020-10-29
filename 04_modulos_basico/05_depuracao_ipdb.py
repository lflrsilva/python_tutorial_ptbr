#
# Autor : Luiz Fernando L. R. Silva
# Data  : 29/10/2020
#
# Uso do módulo IPDB (PDB) para depuração de código
#
# Usando IDE Spyder, use os botões de navegação.
#
# Usando comando de linha, use:
#
# $> python -m ipdb arq_fonte.py
#
# O código entra em modo de depuração, com execução interrompida na primeira
# linha.
# Modo ipdb interativo para entrada de comandos:
#
# q (quit)  - interrompe a execução do depurador
# n (next)  - avança para a próxima linha do script
# p (print) - executa comando print do python
# c (continue) - avança até o próximo breakpoint
# l (list) - mostra em tela as linhas acima e abaixo do ponto atual de execução
# s (step into) - avança para a próxima linha, mas se for um método (função) o
#   comando ENTRA nele.
# r (return) - libera a execução do script até sair do método (função)
# b (breakpoint) - define (ou elimina) pontos de parada em linhas ou método
# a (arguments) - mostra em tela os argumentos que entraram no método (função)
# ENTER - executa o comando anterior

# uso de módulo para matemática simbólica
import sympy as sym

# definicao de simbolos
x = sym.symbols('x')

# solução de equação não linear (usando valores)
# função Eq -> arg1 = arg2
# funcão solverset -> resolve equação
print(sym.solveset(sym.Eq(x**2, 1), x))

# Simplificação de equações
print(sym.simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)))

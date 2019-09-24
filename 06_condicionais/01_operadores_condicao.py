#
# Autor: LF Silva
# Data : 02/06/2018
#
# Operadores em condicionais
#
# - Operadores relacionais:
#    - Igual a          : ==
#    - Maior que        : >
#    - Menor que        : <
#    - Maior ou igual a : >=
#    - Menor ou igual a : <=
#    - Nao igual a      : !=
#
#  - Operadores logicos:
#    - E   : and  (o pessimista)
#    - OU  : or  (o otimista)
#    - NAO : not
#
a = 10
b = 20

# Executando relações, espera-se True ou False
print(f"a = {a:3d}, b = {b:3d}")
print("a == b ", a == b)
print("a > b ", a > b)
print("a < b ", a < b)
print("not(a >= b) ", not(a >= b))
print("not(a <= b) ", not(a <= b))

# Podemos ainda avaliar relações combinadas
print("(a > b) and (a < b)", (a > b) and (a < b))
print("(a > b) or  (a < b)", (a > b) or (a < b))

# Devemos ter cuidado...
x = 0.3333
y = 1.0000/3.0000
print(f"x = {x:5.4f}, y = {y:5.4f}")
print("x == y ", x == y)


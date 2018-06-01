#
# Autor : Luiz Fernando L. R. Silva
# Data  : 31/05/2018
#
# Uso de operadores aritméticos

# Os operadores aritméticos fundamentais +, -, * e / são usados em Python
var1 = 3 + 2
print(var1, type(var1))

var2 = 3 * 2
print(var2, type(var2))

# Python possui uma forma de converter implicitamente o tipo de variável
# numérica, caso seja necessário
var3 = 3 / 2
print(var3, type(var3))

# Contudo, é fortemente recomendado ao programador ficar atento ao tipo de
# variável usado. Para isso, use variáveis correspondendo ao que se deseja
# na expressão.
var4 = 3.0/2.0
print(var4, type(var4))

# Ainda existem os operadores módulo (%) e floor (//)
var5 = 3 % 2      # retorna o resto da divisão
print(var5, type(var5))

var6 = 9 // 2     # retorna o quociente da divisão, arredondando para baixo
print(var6, type(var6))

# O operador expoenciação (**) também está incluído
var7 = 2 ** 3
print(var7, type(var7))

# A precedência de operações para efetuar expressões em Python, segue a
# leitura da esquerda para direita e na ordem **, *, /, %, //, +, -
var8 = 2 + 3*4 - 2**2

# A ordem das operações fica:
# var8 = 2 + 3*4 - 4
# var8 = 2 + 12 - 4
# var8 = 14 - 4
# var8 = 10
print(var8)

# É possível modificar a ordem de precedência usando parênteses
var9 = (2 + 3)*(4-2)**2

# A ordem das operações fica:
# var9 = (2 + 3)*(4-2)**2
# var9 = 5*(4-2)**2
# var9 = 5*2**2
# var9 = 5*4
# var9 = 20
print(var9)

# Recomendação: na dúvida, organize sempre suas expressões usando parênteses

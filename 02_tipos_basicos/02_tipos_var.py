#
# Autor : Luiz Fernando L. R. Silva
# Data  : 31/05/2018
#
# Tipos de variáveis em Python

# Python possui os seguintes tipos de variáveis básicas
#
# - Números
# - Strings (cadeia de caracteres)
# - Listas
# - Tuplas
# - Dicionários

## Numeros
print(" - Números :")
# Os números podem ser usados para efetuar operações matemáticas e avaliar
# expressões. Números podem ser:
# - Inteiros, ex. 123
# - Ponto flutuante (real), ex. 123.0
# - Complexos (imaginário), ex. 123.0j

# Primordialmente, a responsabilidade sobre o tipo de variável usada é
# do programador. Ou seja, a culpa é sua!
int1  = 5
real1 = 5.0
real2 = 3.1416e0
real3 = 6.0221408e23  # no. de avogrado (mol^-1)

print(int1)
print(real1)
print(real2)
print(real3)

## Strings
print("\n \n - Strings :")
# A cadeia de caracteres são numeradas de forma encadeada permitindo acesso
# aos caracteres individualmente. A numeração é iniciada com o índice 0.
# As strings podem ser definidas usando cliques ('') ou aspas ("").
str1 = 'Olá mundo!'
str2 = "Olá lua!"

print(str1)

# Os caracteres podems ser acessados usando o operador [i],
# onde i é o índice de acesso.
print(str2[0])
print(str2[1])
print(str2[int1])

# É possível acessar uma fatia da cadeia de caracteres usando o operador [:]
print(str1[1:int1])
print(str1[1:])

## Booleanas
print("\n \n - Booleanos:")
# As variáveis booleanas são usadas em tarefas de decisão
f = False
t = True

print(type(f), type(t))

# As decisões podem ser obtidas usando operadores lógicos e de comparação,
# assunto abordado mais à frente nesse tutorial
print(f == t)

## Listas
print("\n \n - Listas :")
# Listas são agrupamentos de variáveis de qualquer tipo organizados de forma
# encadeada. Assim como nas strings, o acesso é feito usando o operador [].
list1 = ['abc', 123, 321.4]
list2 = ["Olá", "mundo", "!"]

print(list1)
print(list2)
print(list2[0])
print(list2[0][1])

print(list1)
print(list1[2])

list1[2] = 456.9
print(list1)
print(list1[2])

# Cuidado! Se tentar acessar algum elemento da lista usando um índice que não
# existe, o programa será interropido com uma mensagem de erro!
# print(list1[3])

## Tuplas
print("\n \n - Tuplas :")
# Tuplas são listas que não podem ser editadas. Ou seja, são listas em modo
# de leitura apenas. São usadas especialmente para armazenar informações
# que serão usadas nos cálculos mas não precisam ser editadas. Por ex., tabela
# de propriedades físicas.
tuple1 = ('cba', 321, 123.4)

print(tuple1)
print(tuple1[2])

## Dicionários
print("\n \n - Dicionários :")
# Discionários são listas de variáveis encadeadas cujos índices de acesso
# são definidos pelo programador.
dict1 = {"nome" : "LF", "dre": 12345, 6 : 5.0}

print(dict1["nome"])
print(dict1[6])

# É possível acessar apelas as chaves (índices) ou os valores nos dicionários
print(dict1.keys())
print(dict1.values())

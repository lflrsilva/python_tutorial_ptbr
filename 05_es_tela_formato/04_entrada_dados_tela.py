#
# Autor : LF Silva
# Data  : 13/04/2020
#
# Formato da entrada de dados em tela

# A entrada de dados, por padrão, é para variáveis do tipo string. Portanto, é
# necessário SEMPRE converter a variável para o tipo desejado.
#

# Comando input para entrar com informação em tela
idade = input("Entre com sua idade: ")
# print(f"Você tem {idade:3d} anos")
print(f"O tipo da variável é {type(idade)}")

# Mas e como converter a entrada para determinado tipo?
# Convertendo para variável inteira
age = int(input("Mais uma vez, entre com a sua idade: "))
print(f"Você tem {age:3d} anos.")

# Convertendo para ponto flutuante
weight = float(input("Entre com o seu peso (kg): "))
print(f"Você tem {weight:3.2f} kg.")
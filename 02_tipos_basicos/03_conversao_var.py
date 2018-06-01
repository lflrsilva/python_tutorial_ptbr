#
# Autor : Luiz Fernando L. R. Silva
# Data  : 31/05/2018
#
# Conversao entre tipos de variáveis

# É possível entrar com dados em tela
x = input("Entre com o dado: ")
print(x)

# Contudo, por padrão, a entrada de dados é como uma string. Podemos ver o
# tipo da variável usando a função type
print(type(x))

# Se queremos realizar operações aritméticas, devemos convertera entrada
# de dados para um outro tipo de variável.
y = float( input("Entre com a informação: ") )
print( y, type(y) )

# De forma básica, os tipos podem ser convertidos usando funções
#
# - int(x)   : converte x para número inteiro
# - float(x) : converte x para número real
# - str(x)   : converte x para string
#
# Mais formas de conversão podem ser encontradas no manual de Python.



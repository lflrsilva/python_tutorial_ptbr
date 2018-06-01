#
# Autor : Luiz Fernando L. R. Silva
# Data  : 31/05/2018
#
# Testes iniciais usando Python 3

# Escrevendo em tela
print("Olá mundo!")   # também podemos comentar depois do comando

# Podemos pular linha também
print("Olá \n mundo!")

# Existem identificadores especiais para executar certas tarefas
# dentro de uma cadeia de caracteres.
# \n - pular linha (newline)
# \t - tabulação
# \a - campainha
# \b - backspace
# \r - volta ao inicio da linha
# \v - tabulação vertical
print("Olá \v mundo!")

# Também podemos escrever comandos usando várias linhas
# A continuação de comandos deve ser feita usando \
print("Tem \
um \
unico \
comando \
aqui")

# Podemos atribuir valores às variáveis
var1 = 123
var2 = 123.4
var3 = "123.4"

# e podemos escrever em tela para o usuário
print(var1)
print(var2)
print(var3)

# Se necessário também é possível realizar atribuição múltipla
var4, var5, var6 = 321, 321.0, "321"
print(var4)
print(var5)
print(var6)

# e ainda podemos combiná-las com o texto
print("Essa variável é um número        : ", var1)
print("Essa variável também é um número : ", var2)
print("Mas essa variável é uma string   : ", var3)


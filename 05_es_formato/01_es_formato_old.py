#
# Autor : LF Silva
# Data  : 01/05/2018
#
# Formato da saída de dados

# A formatacão depende do tipo de variável, identificada por
#
# d - número inteiro
# f - número real
# s - cadeia de caracteres
i = 2
x = 0.00001
print("O no. i alocado é %d" % i)
print("O no. x alocado é %f" % x)

# Podemos ainda formatar o espaçamento usado
print("O no. i alocado é %3d" % i)
print("O no. x alocado é %3.10f" % x)

# Para pontos flutuantes, podemos escrever em formato exponencial
print("O no. x alocado é %3.5e" % x)

# E ainda podemos combinar várias saídas de dados em um único print
# Neste caso, deve-se definir uma tupla para a ordem das variáveis
print("Nos. x e i em sequencia = %3d, %3.4e" % (i, x) )

# Vale notar que a formatação apresentada acima foi atualizada em
# Python 3. Apesar de ainda ser possível usar a formatacão antiga, vale
# a pena se atualizar em relação à nova formatação.


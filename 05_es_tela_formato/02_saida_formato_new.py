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
# Uso do identificador de strings f ou F
# indentificação automática do tipo de variável (sem formatar)
print(f"O no. i alocado é {i}")
print(f"O no. x alocado é {x}")

# Podemos ainda formatar o espaçamento usado
print(f'O no. i alocado é {i:3d}')
print(f"O no. x alocado é {x:3.10f}")

# Para pontos flutuantes, podemos escrever em formato exponencial
print(f"O no. x alocado é {x:3.5e}")

# E ainda podemos combinar várias saídas de dados em um único print
# Neste caso, deve-se definir uma tupla para a ordem das variáveis
print(f"Nos. x e i em sequencia = {i:3d}, {x:3.4e}")

# Vale notar que ainda existem outras possibilidades de formatação
# usando o comando format. Vale verificar na documentação de
# Python 3.
print("O no. aqui colocado = {:d}".format(i))

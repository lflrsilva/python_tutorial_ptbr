#
# Autor : Luiz Fernando L. R. Silva
# Data  : 22/06/2020
#
# Manipulações usando listas e dicionários

## Usando dicionários
dict1 = {'Nome': 'LF', 'ID': 1234567, 'Cargo': 'Professor'}
dict2 = {}

# preenchendo dicionário a partir de existente
# dict2 precisa já existir!!
dict2.update(dict1)
print(dict2)

# limpando dicionário
dict2.clear()
print(dict2)

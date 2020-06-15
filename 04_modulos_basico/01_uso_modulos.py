#
# Autor : LF Silva
# Data  : 01/05/2018
#
# Usando módulos em Python

# Módulos em Python são agregados de variáveis e/ou funções específicas
# já implementadas que podem ser usadas. Para tal, você deve importar o
# módulo para o seu programa.
#
# import math
#
# e, com isso, as funções matemáticas podem ser usadas. Por exemplo,
# math.log(x) fornece o logaritmo neperiano de x. Para não precisar
# escrever math. ..., é possível usar uma abreviação.

import math as m   # importando module matemático

print(m.fabs(-2.0))

import os # importando module de sistema operacional

# Podemos ver as funções do módulo usando o comando dir
print(dir(os))
print(os.name)
print(os.uname())

# Para ver os modules disponíveis por padrão, acesse a documentação do
# Python em:
#
# https://docs.python.org/3/library/index.html

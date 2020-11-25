#
# Autor: LF Silva
# Data  : 23/11/2020
#
#  Introdução ao uso de Numpy - Cópia de arrays
# O problema de shallow e deep copy
import numpy as np

# Python é bem espertinho ao alocar a memória para suas variáveis.
# Mas isso pode gerar algumas situações complicadas com o
# compartilhamento de informações na memória.
x = 10
y = x
print("ID x = ", id(x))
print("ID y = ", id(y))
print("Local de memoria compartilhado (x,y) : ", x is y)

y = 11
print(x, y)
print("ID x = ", id(x))
print("ID y = ", id(y))
print("Local de memoria compartilhado (x,y) : ", x is y)

# A situação pode ser mais complexa ao alocar o endereço para
# um array (sua base) e seus elementos.
# criação de array
arr1 = np.array([3, 4, 5, 7, 10, 21], dtype='float')
print("arr1 = ", arr1)
print("ID arr1    = ", id(arr1))
print("ID arr1[3] = ", id(arr1[3]))

# Operações de atribuição em Python não copiam objetos. Se criam conexões entre
# o objeto original e o alvo diretamente na memória (chamada de referência).
# Ou seja, ao manipular as variáveis alocadas na memória, tanto o objeto
# original quanto o alvo são alterados. arr1 = objeto original; arr2 = alvo;
print("Análise por atribuição: ")
arr2 = arr1
arr2[1] = 3.0
print("arr1 = ", arr1)
print("arr2 = ", arr2)
print("ID arr1 == ID arr2 : ", arr1 is arr2)

arr1[4] = 3.0
print("arr1 = ", arr1)
print("arr2 = ", arr2)

# Ou seja, usar o operador de atribuição pode levar a erros de lógica na
# execução do script (afinal, a sintaxe está correta)!

# Mas e como contornar isso em arrays Numpy?
# O método view() cria o que chamamos de shallow copy em que se cria um
# novo array, mas a referência entre os elementos são compartilhadas.
print("Análise por shallow copy: ")
brr1 = np.array([3, 6, 9, 12], dtype='float')
brr2 = brr1.view()
print("brr1 = ", brr1)
print("brr2 = ", brr2)
print("ID brr1 == ID brr2 : ", brr1 is brr2)

# e se alterar os elementos?
brr2[1] = 8
print("novo brr1 = ", brr1)
print("novo brr2 = ", brr2)

# Isso não resolve o problema. Usando Numpy, é possível usar o método
# copy(). O comando cria uma nova variável (alvo) e copia o conteúdo
# do objeto original para o alvo. brr1 = objeto original; brr3 = alvo;
# Para arrays (int, floats e strings), isso contorna o problema.
print("Análise por deep copy: ")
brr3 = np.copy(brr1)
print("brr1 = ", brr1)
print("brr3 = ", brr3)
print("ID brr1 == ID brr3 : ", brr1 is brr3)

# e se alterar os elementos?
brr3[1] = 33
print("novo brr1 = ", brr1)
print("novo brr3 = ", brr3)

# Cuidados a serem tomados!
# - Comando copy com objetos imutáveis e mutáveis
# - Eficiência computacional
# - Módulo copy
# - Busque mais detalhes com o amigo Google

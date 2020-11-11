#!/usr/local/bin/python3
"""
 Autor : LF Silva
 Data  : 10/11/2020
         11/11/2020

 Comando print

 Absolutamente importante para criar interfaces por comando de linha!

 print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

 em que:

 * objects - o que deve ser apresentado em tela (ou arquivo). * indica que pode 
             existir mais de um objeto.
 * sep -     como os objetos são separados. Valor padrão: ' '
 * end -     o que é adicionado ao fim do objeto apresentado. Valor padrão: '\n'
 * file -    deve ser um objeto com método write(string).
             Se omitido, sys.stdout (saída em tela ) é usado.
 * flush -   Se True, a saída imediata é forçada.  Valor padrão: False

 Mais detalhes em:
 https://realpython.com/python-print/
 https://www.programiz.com/python-programming/methods/built-in/print

"""

# O comando print, por padrão, sempre inclui um identificador
# de nova linha (\n) ao fim do comando
print("Oi, gente! O cursor vai para a próxima linha")

# Mas o comando print tem argumentos opicionais também...
print("Aqui não pula linha.", end=" ")
print("Afinal, tem espaço como identificador final...")

# Já pensou em montar uma lista de tarefas ou de compras?
print("Lista de compras", end="\n * ")
print("Cerveja", end="\n * ")
print("Vodka", end="\n * ")
print("Wisky", end="\n * ")
print("Engov")

# Ainda podemos redefinir como separar os itens no print
# por padrão, usa-se a string espaço " " (ou None)
print("Oi ", "gente", "!")
print("Oi ", "gente", "!", sep="")

# E se quiser trabalhar com hierarquia de diretórios?
print("", "home","users","admin", sep="/")

# E se vc precisar criar um arquivo de dados no formato
# CSV (comma separated values)?
print(1,"dado 1","dado 2", sep=",")

#
# Autor : LF Silva
# Data  : 13/04/2020
#
# Saída de dados em arquivo
import numpy as np

# Vamos criar um arquivo e escrever dados nele. Por padrão, iremos trabalhar com arquivos do tipo texto para escrever os dados. Mas para que isso? E se você quiser guardar os dados para usar em outro programa (MS Excel, Origin, Statistica etc)? E se você precisa realizar backup com frequência? E se...
#

# Abrir um arquivo chamado nome_arquivo.txt
# Modos de manipulação do arquivo:
# w  - write : escrita no arquivo (caso já exista, cria por cima)
# r  - read  : leitura no arquivo (arquivo já deve existir)
# a  - append: escrita ao fim do arquivo (caso já existam dados)
# r+ - read+ : leitura E escrita
arq1 = open("nome_arquivo.txt", "w")

# Escrevendo informação em arquivo
# Por padrão, a escrita deve ser em formato string
arq1.write("Olá mundo!\n")

y = 5.0
# arq1.write(y)  ## ERRO
print(f"{y:.2f}", file=arq1)

# fechando instância de arquivo
arq1.close()

# calculo da cinética de reação qualquer
t  = np.linspace(0,10,200)
ca = 15*np.exp(-t)

# Abrindo arquivo para modo escrita - modo recomendado
with open("dados_cinetica.dat", "w") as arq2:
    for (ti, cai) in np.nditer([t,ca]):
        print(f"{ti:3.3e}\t{cai:}", file=arq2)

# A instância do arquivo é automaticamente fechada ao sair do comando with

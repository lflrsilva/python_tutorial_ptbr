#
# Autor : LF Silva
# Data  : 14/04/2020
#
# Entrada de dados em arquivo

# Vamos ler um arquivo com dados e processar em Python. Por padrão, iremos trabalhar com arquivos do tipo texto para leitura dos dados mas existem várias bibliotecas para ler outros formatos, como planilhas Excel, por exemplo.
#

# Abrir um arquivo chamado dados_simulacao.txt
# Modos de manipulação do arquivo:
# w  - write : escrita no arquivo (caso já exista, cria por cima)
# r  - read  : leitura no arquivo (arquivo já deve existir)
# a  - append: escrita ao fim do arquivo (caso já existam dados)
# r+ - read+ : leitura E escrita
with open("dados_simulacao.txt", "r") as indata:
    # ler todos os dados do arquivo de uma vez    
    all_data = indata.read()
    print(all_data)
    
    # ler uma única linha do arquivo
    # line = indata.readline()
    # print(line)
    
    # ler todas as linhas, indo de linha em linha
    # for line in indata:
    #     print(line)
    #     # separar a string pelo "espaço"
    #     args = line.split(" ")
    #     print(args)
    #     # converter as strings em float
    #     x = float(args[0])
    #     y = float(args[1])
    #     print(x,y)
    #     print(type(x))
        
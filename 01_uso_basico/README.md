Instalação e uso básico de Python
=================================

## O que é Python?
[Python](https://www.python.org/) é uma linguagem de programação de alto 
nível, interpretada, de script, imperativa, orientada a objetos, funcional, 
de tipagem dinâmica e forte.  Apesar de várias partes da linguagem possuírem 
padrões e especificações formais, a linguagem como um todo não é 
formalmente especificada. O padrão de fato é a implementação 
[CPython](https://www.python.org/).

A linguagem foi projetada com a filosofia de enfatizar a importância do 
esforço do programador sobre o esforço computacional. Prioriza a legibilidade 
do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e 
clara com os recursos poderosos de sua biblioteca padrão e por módulos e 
frameworks desenvolvidos por terceiros.

Uma das motivações em iniciar o uso de Pyhton é a facilidade de
desenvolvimento, independente se você já tem alguma experiência com
programação. Vale uma visita ao site do [Python](https://www.python.org/about/)
pois estão disponíveis vários guias para iniciantes assim como sua 
documentação completa.

Como referência ao aprendizado, sugiro uma busca e leitura nos seguintes sites:

* Python : <https://www.python.org/>
* Python Brasil : <https://python.org.br/>
* Tutorials Point : <https://www.tutorialspoint.com/python3/index.htm>
* Anaconda : <https://www.anaconda.com/>
* Spyder IDE : <https://www.spyder-ide.org/>

### Python para desenvolvimento científico
Python é uma linguagem de programação completa, que contém a funcionalidade
exigida por programadores para escrever todos os tipos de códigos, desde fazer
filmes até para previsão do tempo. Nesse sentido, apesar de Python ser uma
linguagem relativamente moderna, já foram desenvolvidas várias bibliotecas 
específicas para programas de cunho científico, como 
[NumPy](http://www.numpy.org), [Matplotlib](https://matplotlib.org),
[SciPy](https://www.scipy.org) entre outras.

Como Python pode ser usado em diferentes situações, as bibliotecas para
desenvolvimento científico não estão instaladas por padrão. Desta forma, é
necessário gerenciar quais são as bibliotecas que quer manter incorporadas à
sua instalação de Python.

## Instalação
Uma das dúvidas mais recorrentes dentre os iniciantes na linguagem é a 
respeito da escolha de versão: "Estou começando na linguagem, devo usar a 
versão 2 ou 3 de Python?" Para responder a esta pergunta é importante entender
o estado atual da linguagem:

* Python 2 foi o padrão da linguagem por muito tempo.
* Python 3 introduziu algumas mudanças que quebraram a compatibilidade com a 
  versão anterior o que criou a nessecidade de se manter duas versões da 
  linguagem.
* Python 2 receberá atualizações de segurança até 2020 quando seu suporte 
  será descontinuado.
* Python 3 está constantemente evoluindo e recebendo novas funcionalidades, 
  que não estarão presentes na versão anterior.

Sabendo disso, a recomendação é de dar sempre que possível preferência ao 
Python 3, por ser o futuro da linguagem e pelo fato de sua versão anterior 
estar em processo de descontinuação.

### Instaladores
Você pode obter o arquivo de instalação diretamente do site do Python. Nesse
caso, você deve gerenciar manualmente as bibliotecas e módulos instalados. Como
o foco neste tutorial é desenvolvimento científico, recomendo a instalação
da IDE (Interface de desenvolvimento) [Spyder](https://www.spyder-ide.org/) em
conjunto com [Anaconda](https://www.anaconda.com/). O principal motivo é que a
IDE Spyder já incorpora os principais módulos de desenvolvimento científico e,
portanto, atende às necessidades dos tutoriais.

Ao instalar o Anaconda, você pode navegar pelos módulos e IDEs disponíveis para
instalação. Para uma melhor visão da navegação no Anaconda, acesse
<https://docs.anaconda.com/anaconda/navigator/>

## Uso básico
Após a instalação, o Python é acessível primordialmente através de comandos
escritos em tela. Para Windows, os comandos podem ser inseridos no *Prompt de
comando* do Anaconda ou na área de comandos do *Spyder*. Para Linux ou MacOS,
os comandos podem ser inseridos via terminal ao acessar o programa *python*.
Tome cuidado pois diferentes versões de python podem coexistir e você deve
verificar a versão que está executando. Para tal (Linux e MacOS), digite no
terminal:

    $ python --version

### Interpretadores
A primeira etapa é usar o Python como interpretador de comandos. Ao acessar a
tela de comandos, o usuário é capaz de executar os comandos por vez. Por
exemplo,

    >>> a = 1
    >>> print a

Em dois comandos, você criou uma variável chamada 'a' e atribuiu o valor de '1'
e, na sequência, executou um comando de saída de dados em tela mostrando o
valor da variável 'a'. De fato, é possível executar qualquer código em Python
pela tela de comandos. Contudo, isso se torna complicado quando se pretende
usar muitos comandos em uma programação mais elaborada. Por isso, é melhor
criar scripts que contém a sequência de comandos a ser executada. Para sair do
interpretador, digite e execute:

    >>> exit()

### Scripting
Os scripts nada mais são que arquivos texto contendo a sequência de comandos
que se quer executar. Note que os scripts podem ser criados com qualquer editor
de textos simples (Bloco de Notas, Notepad++, gedit, Sublime Text etc). O
Spyder já possui um editor de textos incorporado com atalhos para execução do
script.

Vou considerar um arquivo de texto com os dois comandos acima. Salve o arquivo
com extensão `.py` para identificá-lo como um script de Pyhton. Para
executá-lo, você pode executar o seguinte comando no terminal:

    $ python script.py

Com isso, os comandos dentro do arquivo `script.py` são executados
sequencialmente.

Neste tutorial, você deve abrir os scripts de execução em algum editor de
textos simples onde existem comentários (linhas começadas com `#`) sobre a
linguagem e algoritmos para implementação de códigos em python.


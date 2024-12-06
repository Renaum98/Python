'''
    Funçoes para manipulação de textos
Por meio da linguagem Python, podemos manipular dados em um arquivo texto, mostrando as operações básicas de leitura e escrita.

Esse arquivo texto é conhecido como arquivo sequencial, porque a leitura tem de ser feita de forma sequencial, do início ao fim do arquivo.

Para trabalharmos com arquivos texto na linguagem Python utilizamos funções.

A função open() é utilizada para a abertura dos arquivos.

Sua sintaxe é:

arquivo = open(‘arquivo.txt’, ‘w’)
A função open(), após a declaração da variável que receberá a função, necessita de dois parâmetros: primeiramente o nome do arquivo e, depois, o modo como estamos abrindo esse arquivo.

Na sintaxe apresentada acima foi utilizado o ‘w’ para fazer a escrita em um arquivo.

Caso o arquivo não exista nesse modo, o código criará um arquivo com o nome escrito no primeiro parâmetro.

A função write() é utilizada para gravar informações em um arquivo existente.

Sua síntaxe é:
arquivo.write (‘Curso Python n’)
arquivo.write (‘Aula Prática’)

Na função, adicionamos o nome do arquivo e, logo após o símbolo do ponto final, fazemos a chamada da função write. Em seguida, adicionamos o texto que deverá ser gravado entre aspas simples.

A função close() é muito importante para encerrar o arquivo após sua utilização.

Atenção: Nunca abra o arquivo com a função open e depois o faça de novo, sem antes fechar a instância anterior.

Sua síntaxe é:
arquivo.close()

Um dos motivos da necessidade da função close() é que se tentarmos escrever em um arquivo e não o fecharmos depois de terminar a escrita, as informações não chegarão ao arquivo e nada será escrito.
'''
'''
A função read() realiza a leitura

de todo conteúdo do arquivo.


Sua sintaxe é:

leitura=open(‘arquivo.txt, ‘r’)

print leitura.read()

leitura.close()
Utilizamos o parâmetro ‘r’ que representa que o arquivo está sendo aberto em modo leitura.

Desta forma, não é possível modificar os dados contidos no arquivo.

Nome do arquivo

Ao utilizar a função read(), o nome do arquivo deve ser:

1) Uma string com o caminho completo (por exemplo, C Documentos teste txt)
ou
2) O caminho em relação ao diretório atual (nomes txt do arquivo que se deseja abrir).'''

arquivo = open('arqText.txt','w')

arquivo.write('Curso Python \n')
arquivo.write('Aula Pratica')
arquivo.close()

#leitura do arquivo de texto

leitura=open('ArqText.txt','r')
print(leitura.read())
leitura.close()
'''
Além dos comandos vistos até aqui (w e r), também temos disponíveis outros comandos que podemos utilizar nos parâmetros.

r	-Abre o arquivo somente para leitura.
O arquivo deve já existir.

r+	-Abre o arquivo para leitura e escrita. O arquivo deve já existir.
A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.

w	-Abre o arquivo somente para escrita, no início do arquivo.
Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.

w+	-Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.

a	-Abre o arquivo para escrita no final do arquivo.
Não apaga o conteúdo preexistente.

a+	-Abre o arquivo para escrita no final do arquivo e leitura.

'''
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'arquivos.txt'

if arqExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas',
                     'Cadastrar nova pessoa',
                     'Sair do Sistema'])
    if resposta == 1:
        #opcão de listar o conteúdo de um arquivo!
        lerArquivo(arq) 
    elif resposta == 2:
        cabeçalho(colored('Novo Cadastro','green'))
        nome = input('Nome: ').title().strip()
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho(colored('Saindo do Sistema ... Até logo!','green'))
        break
    else:
        print(colored('ERRO!, Digite uma opção válida','red'))
    sleep(1)
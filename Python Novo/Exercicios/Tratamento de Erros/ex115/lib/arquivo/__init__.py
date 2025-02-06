from lib.interface import cabeçalho
from termcolor import colored

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else: 
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print(colored('Houve um erro na abertura do arquivo','red'))
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(colored('Houve um erro na hora de escrever os dados','red'))
        else:
            print(colored(f'Novo registro de {nome} adicionado','green'))
            a.close()
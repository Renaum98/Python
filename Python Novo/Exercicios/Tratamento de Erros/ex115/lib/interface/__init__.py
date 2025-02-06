from termcolor import colored

def leiaInt(msg):
    while True:
        try: 
            n = int(input(msg))
        except(ValueError,TypeError):
            print(colored('ERRO:Por favor, digite um numero inteiro valido','red'))
            continue
        except(KeyboardInterrupt):
            print(colored('Entrada de dados interrompida pelo usuario','red'))
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(colored(f'{c}','yellow'),'-',colored(f'{item}','blue'))
        c += 1
    print(linha())
    opc = leiaInt(colored('Sua opção: ','yellow'))
    return opc
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO, Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor
# Programa principal
n = leiaInt('Digite um numero: ')
print(f'Você digitou o numero \033[0;32m{n}\033[m')


'''while True:
    n = input('Digite um numero: ')
    if n.isnumeric():
        print(f'Voce digitou o numero \033[0;32m{n}\033[m')
        break
    else:
        print(f'\033[0;30;41m ERRO Digite um numero Valido \033[m')'''
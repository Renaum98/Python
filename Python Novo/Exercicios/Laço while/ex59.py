n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
while n1 or n2 > 0:
    print('[1]Soma')
    print('[2]Multiplicar')
    print('[3]Maior')
    print('[4]Novos Numeros')
    print('[5]Sair do Programa')
    a = int(input('Escolha uma operação:'))
    while a <= 0 or a > 5:
        print('Escolha uma operação valida')
        a = int(input('Escolha uma operação:'))
    while a == 1:
        print('A soma de {} com {} é: {}'.format(n1,n2,(n1+n2)))
        a = int(input('Escolha uma operação:'))
    while a == 2:
        print('A Multiplicação de {} e {} é: {}'.format(n1,n2,(n1*n2)))
        a = int(input('Escolha uma operação:'))
    while a == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n1 == n2:
            print('{} é igual a {}'.format(n1,n2))
        else:
            print('{} é maior que {}'.format(n2,n1))
        a = int(input('Escolha uma operação:'))

    

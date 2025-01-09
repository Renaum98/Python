#30 - Ecreva um programa que leia um numero inteiro qualquer e descuba se ele é par ou impar

n1 = int(input('Digite um numero inteiro:'))

n2 = n1%2

if n2 == 0:
    print('O numero {} é Par'.format(n1))
else:
    print('O numero {} é Impar'.format(n1))
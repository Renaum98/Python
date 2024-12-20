#32 - Faça um programa que leia um ano qualquer e mostre se ele é um ano bissexto

ano = int(input('Digite um ano:'))


if ano % 4 == 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto'.format(ano))
else:
    print('O ano de {} não é Bissexto'.format(ano))
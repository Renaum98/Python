#23-Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

'''
FORMA ERRADA
n = input('Digite um numero de 0 a 9999:')
unidade = n[3:]
dezena = n[2:3]
centena = n[1:2]
milhar = n[0:1]
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
'''

num = int(input('Digite um numero de 0 a 9999:'))
n = str(num)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
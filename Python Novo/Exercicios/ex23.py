#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = input('Digite um numero de 0 a 9999:')
unidade = n[3:]
dezena = n[2:3]
centena = n[1:2]
milhar = n[0:1]
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

#28 - escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5, e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
#o programa devera escrever se o usuario venceu ou perdeu

import random

print('Tente adivinhar o numero que o Computador ira gerar')

n1 = int(input('Digite um numero inteiro de 0 a 5:'))
n2 = random.randint(0,5)

if n1 == n2:
    print('Parabens, você acertou o numero que o computador gerou que foi {}'.format(n2))
else:
    print('Infelizmente você não acertou o numero que o computador gerou que foi {}'.format(n2))
    print('Continue tentando')

print('Obrigado por testar o programa <3')
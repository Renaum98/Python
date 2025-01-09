#sorteando um valor em uma lista
from random import choice
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
al5 = input('Quinto aluno: ')

lista = [al1, al2, al3, al4, al5] #para criar uma lista use o [] com as variaveis que pertencem a lista

sorteio = choice(lista) #com o random.choice é escolhido somente uma opção dentre as listadas

print('O aluno escolhido foi {}'.format(sorteio))
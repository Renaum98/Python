#Sorteando uma ordem na lista
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]

shuffle(lista)#shuffle é embaralhar, sendo assim sera embaralhado a lista
print('A ordem do trabalho sera {}'.format(lista))
#Crie um programa que leia o nme de uma cidade e diga se ela começa ou não com 'santo'

cidade = input('Digite o nome de um cidade: ').strip()
pcidade = cidade.split()



print('santo' in pcidade[:1])
#27-Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ').title().strip()
nome_lista = nome.split()
print('Seu primeiro nome é {}'.format(nome_lista [0]))
print('Eu ultimo nome é {}'.format(nome_lista[-1]))
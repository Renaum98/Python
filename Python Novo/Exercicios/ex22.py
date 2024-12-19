#22-Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = input('Digite um nome completo: ')

print('Seu nome em maiusculas é:',nome.upper())

print('Seu nome em minusculas é:',nome.lower())

nome_sem_espaço = nome.replace(" ","")
print('Seu nome tem:',len(nome_sem_espaço),'letras')

nome_lista = nome.split()

primeiro_nome = nome.split()[0]
print('Seu primeiro nome é',nome_lista[0], 'e ele tem',len(primeiro_nome),'letras')
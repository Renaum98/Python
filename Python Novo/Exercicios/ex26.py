#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase:').upper().strip()

print('Quantas vezes a letra A aparece?',frase.count('A'))

print('Em que posição a letra A aparece pela primeira vez?',frase.find('A')+1)

print('Em que posição a letra A aparece a ultima vez?',frase.rfind('A')+1)

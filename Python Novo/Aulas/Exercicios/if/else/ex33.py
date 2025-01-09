#33-Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

n1=input('Digite um numero:')
n2=input('Digite um numero:')
n3=input('Digite um numero:')

'''
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))
'''

#maior numero
if n1 >= n2 and n1>=n3:
    maior = n1
elif n2 >= n1 and n2>=n3:
    maior = n2
else:
    maior = n3

#menor numero
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))


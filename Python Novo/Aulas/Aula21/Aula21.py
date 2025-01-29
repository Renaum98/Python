# Aula 21: Módulos e pacotes
# Módulos de forma geral servem para dividir um programa fazendo com que fique mais facil e organizado a sua execução
# Exemplo de módulo:
# uteis.py
# Pacotes são pastas que contém módulos

from uteis import numeros
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobros de {num} é {numeros.dobro(num)}.')
print(f'O triplo de {num} é {numeros.triplo(num)}.')

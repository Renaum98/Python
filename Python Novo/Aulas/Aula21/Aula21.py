# Aula 21: Módulos e pacotes
# Módulos de forma geral servem para dividir um programa fazendo com que fique mais facil e organizado a sua execução
# Exemplo de módulo:
# uteis.py
# Pacotes são pastas que contém módulos

import uteis
num = int(input('Digite um número: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobros de {num} é {uteis.dobro(num)}.')
print(f'O triplo de {num} é {uteis.triplo(num)}.')

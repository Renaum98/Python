ficha = list()
while True:
    nome = input('Nome: ').title().strip()
    nota1 = float(input('Nota 1: ')).strip()
    nota2 = float(input('Nota 2: ')).strip()
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resp = ' '
    while resp not in 'S,N':
        resp = input('Quer continuar? [S,N]').upper()[0].strip()
    if resp in 'N':
        break
print('-=' * 10, 'Boletim Escolar','=-' * 10 ) 
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 26)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*len(opc))
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('Finalizando')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
lista = []
alunos = []
notas = []
while True:
    alunos.append(input('Digite o nome do aluno: ').title())

    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    notas.append((notas[0] + notas[1]) / 2)
        
    alunos.append(notas[:])
    lista.append(alunos[:])
    notas.clear()
    alunos.clear()



    continuar = ' '
    while continuar not in 'S,N':
        continuar = input('Deseja continuar?[S/N]').upper()[0]
    if continuar in 'N':
        break
print('-'*40)
print(f'{'No.':<5}{'Nome':<20}{'Média':>5}{'Situação':>10}')
print('-'*40)
for n, a in enumerate(lista):
    print(f'{n:<5}{a[0]:.<20}{a[1][2]:>5.1f}{'Aprovado' if a[1][2] > 6 else 'Reprovado':>10}')
while True:
    selec= int(input('Mostrar a nota de qual aluno? (999 interrompe)'))
    if selec <len(lista):   
        print(f'As notas de {lista[selec][0]} foram {lista[selec][1][0]} e {lista[selec][1][1]}')
    else:
        print('Esse aluno não existe, Digite um aluno valido')
    if selec == 999:
        break
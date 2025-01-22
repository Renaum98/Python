tabela = {}
jogos = []
cadastro = []
while True:
    tabela['nome']= input('nome: ').title()
    tabela['total'] = int(input(f'Quantas partidas {tabela['nome']} jogou? '))
    for c in range(0,tabela['total']):
        gols = int(input(f'Quantos gols no jogo {c+1} '))
        jogos.append(gols)
    tabela['gols'] = jogos[:]
    cadastro.append(tabela.copy())
    jogos.clear()
    continuar = ' '
    while continuar not in 'S,N':
        continuar = input('Deseja continuar? [S/N]').upper()[0]
    if continuar in 'N':
        break
for i in tabela.keys():
    print(f'{i:<15} ',end='')
print()
print('-'*40)
for n, c in enumerate(cadastro):
    print(f'{n:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
while True:
    print('-'*40)
    selec= int(input('Mostrar dados de qual jogador? (999 interrompe)'))
    if selec <= len(cadastro):
        print(f'-- LEVANTAMENTO JO JOGADOR {cadastro[selec]['nome']}: ')
        for n, c in enumerate(cadastro[selec]['gols']):
            print(f'   No jogo {n+1} fez {c} gols.')  
    elif selec == 999:
        print('<< VOLTE SEMPRE >>')
        break  
    else:
        print(f'Não existe jogador com o codigo {selec}, Tente novamente')
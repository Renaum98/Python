import random
lista = ['PAR','IMPAR']
cont = 0

print("-"*30)
print('Jogue Par ou Impar comigo')
print("-"*30)

while True:
    soma = 0
    comp1 = random.randint(1,10)
    comp2 = random.choice(lista)
    num = int(input('Digite um numero de 1 a 10: '))
    if num <0 or num > 10:
        print('Digite um numero de 1 a 10: ')
    else:
        choice = str(input('Você quer PAR ou IMPAR?: ')).upper()
        while True:
            if choice in lista:
                break
            else:
                print('Digite PAR ou IMPAR: ',end='')
                choice = input().upper()
        soma = comp1 + num
        print(f'O numero é {soma}')
        if choice == comp2:
            print(f'Eu escolhi {comp2} e você {choice}')
            print('Rodada empatada')
            print('-'*30)
        else:
            if soma % 2 == 0 and choice == 'PAR':
                print(f'Eu escolhi {comp2} e você {choice}')
                print('Você VENCEU a rodada 🥳')
                cont+=1
                print('-'*30)
            elif soma % 2 != 0 and choice == 'IMPAR':
                print(f'Eu escolhi {comp2} e você {choice}')
                print('Você VENCEU a rodada 🥳')
                cont+=1
                print('-'*30)
            else:
                print(f'Eu escolhi {comp2} e você {choice}')
                print('Você PERDEU a rodada ☹️')
                print('-'*30)
                break
print("_"*30)
print(f'Fim de jogo, você obteve {cont} vitorias seguidas')
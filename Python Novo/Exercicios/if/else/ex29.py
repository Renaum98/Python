#29-Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por cada km acima do limite
from termcolor import colored

carro = int(input('Digite a velocidade do carro:'))

if carro > 80:
    velocidade = float(carro-80)*7
    print(colored('Você foi multado por estar a {}km/h em uma via maxima de {}km/h e tera que pagar R${:.2f}'.format(carro,velocidade),'red'))

print(colored('Siga boa viagem!','green'))

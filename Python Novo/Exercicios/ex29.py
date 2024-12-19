#29-Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por cada km acima do limite

carro = int(input('Digite a velocidade do carro:'))

limite = 80

if carro > 80:
    velocidade = float(carro-limite)*7
    print('Você foi multado por estar a {}km/h em uma via maxima de {}km/h e tera que pagar R${:.2f}'.format(carro,limite,velocidade))

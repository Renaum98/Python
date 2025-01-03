#31 - Desenvolva um programa que pergunte a distancia de uma viagem em km.Calcule o preço da passagem cobrando R$0,50 por km para viagens de ate 200km, e R$0,45 para viagens mais longas

distancia = int(input('Digite quantos kilometros foram percorridos:'))

if distancia <= 200:
    #valor = 0.50 * distancia
    print('O valor a ser pago por {}km percorridos é de R${:.2f}'.format(distancia,distancia*0.50))

else:
    #valor = 0.45 * distancia 
    print('O valor a ser pago por {}km percorridos é de R${:.2f}'.format(distancia,distancia*0.45))


#35 - Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo

r1 = int(input('Digite o valor da reta:'))
r2 = int(input('Digite o valor da reta:'))
r3 = int(input('Digite o valor da reta:')) 

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('As retas formam um triangulo')
else:
    print('As retas não formam um triangulo')

print('Obrigado por testar')

# outra forma de representar porem pode ficar mais complexo e redundante
'''
if r1+r2>r3:
    if r2+r3>r1:
        if r3+r1>r2:
            print('As retas formam um triangulo')
        else:
            print('As retas não formam um triangulo')
'''
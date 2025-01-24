num = 0
cont = 0
soma = 0
print('~'*50)
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont+=1
    soma+=num
print(f'Você digitou {cont} numeros e a soma desses valores é {soma}')
print('Fim')
print('~'*50)
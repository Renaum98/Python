
#Condições Simples e Compostas

#Condições referem-se a estruturas de controle de fluxo que permitem que o programa tome decisões com base em testes lógicos. Elas verificam se uma condição é verdadeira ou falsa e, dependendo do resultado, executam blocos diferentes de código.
# A estrutura básica de uma condição em Python é:

#if: Verifica se uma condição é verdadeira.
#elif: (opcional) Verifica uma condição alternativa, se a primeira condição não for verdadeira.
#else: (opcional) Executa um bloco de código quando todas as condições anteriores são falsas.


n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m =(n1+n2)/2

print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim')

#print('Parabens' if m >= 6 else 'Estude mais') outra forma de escrever o mesmo codigo, chama de condição simplificada




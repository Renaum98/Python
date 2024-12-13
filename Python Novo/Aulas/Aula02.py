#tipos primitivos
#int - representa numeros inteiros
#float - representam numeros reais ou ponto flutuante
#bool - representam valores booleanos (False,True)
#str - representa qualquer caracterie como letra, pontos e até numeros que não vão ser calculados 

#EXEMPLO de uso com o .format

a = int(input('Escreva um valor Numerico:'))
b = int(input('Escreva outro valor Numerico:'))
r = a+b

print('A soma de {} e {} é: {}'.format(a, b, r))
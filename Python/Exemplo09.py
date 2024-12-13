# Estrutura de decisão composta
# Neste caso, utilizaremos o comando else, que significa “se não”. Assim, se a condição for falsa, serão executados os comandos que estiverem posicionados logo após a instrução else.

#idade = int(input('Digite a idade da pessoa:'))

#if idade > 18:
    #print('Maior idade')
#else:
    #print('Menor idade')

notaA = float(input('Informe a primeira nota: '))
notaB = float(input('Informe a segunda nota: '))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >=7.0:
    print('A Média: %.1f - Aprovado'% mediafinal)
else:
    print('A Média: %.1f - Reprovado'% mediafinal)
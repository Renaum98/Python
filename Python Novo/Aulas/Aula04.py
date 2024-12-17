#OPERADORES
# + = SOMA
5+2 

# - = SUBTRAÇÃO
5-2

# * = MULTIPLICAÇÃO
5*2

# / = DIVISÃO
5/2

# ** = POTENCIA
5**2

# // = DIVISÃO INTEIRA
5//2

# % = RESTO DA DIVISÃO
5%2

#ORDEM DE PRECEDENCIA
'''
1 = ()
2 = **
3 = * / // %
4 = + -
'''
nome = 'Bento'
print('Prazer em te conhecer {:^30}!'.format(nome)) #serve pra centralizar o texto e o valor 30 é o numero de caracteres que vai ter

nome2 = 'Bento'
print('Prazer em te conhecer {:>30}!'.format(nome2)) # a seta serve pra colocar o texto fixado na direita

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))

print('A soma de {} e {} é {}!'.format(n1,n2,n1+n2)) # é possivel fazer contas direto no comando sem criar uma variavel como mostrado a cima

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A Soma de {} e {} é:\n{}'.format(n1,n2,s))
print('A Subtração de {} e {} é:\n{}'.format(n1,n2,sub))
print('A Multiplicação de {} e {} é:\n{}'.format(n1,n2,m))
print('A Divisão de {} e {} é:\n{}'.format(n1,n2,d))
print('A Divisão Inteira de {} e {} é:\n{}'.format(n1,n2,di))
print('A Exponenciação de {} e {} é:\n{:.3f}'.format(n1,n2,e))
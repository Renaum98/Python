# Utilizando os comandos if - elif - else
# Adicionalmente, se existir mais de uma condição alternativa que precise ser verificada, utilizamos a condição elif, pois ela avalia as expressões intermediárias antes do comando else.

idade = int (input ('Digite a idade da pessoa:'))
if idade > 18:
    print('Maior idade')
elif idade >=16:
    print('Infanto Juvenil')
else:
    print('Menor idade')
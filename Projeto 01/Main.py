class Main:
    pass

print('Testando o Projeto')

from Cliente import Cliente

from Conta import Conta

c1 = Cliente('João', '114444-2222') # aqui é registrado a instancia relacionada a classe criada em Cliente
c2 = Cliente('Maria','115646-1045')

conta = Conta(c1._nome, 6565,0)

print(conta.titular , 'Numero:',conta.numero,'Seu Saldo',conta.saldo)
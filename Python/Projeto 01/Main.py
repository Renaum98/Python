class Main:
    pass

print('Testando o Projeto')

from Cliente import Cliente

from Conta import Conta

c1 = Cliente('João', '114444-2222') # aqui é registrado a instancia relacionada a classe criada em Cliente
c2 = Cliente('Maria','115646-1045')

conta = Conta(c1.get_nome(), 6565,0)

conta.deposita(100)
conta.saque(50)
conta.extrato()
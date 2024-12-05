#Para entrada de dados não string é preciso alterar o tipo de entrada na variavel

codigo = int(input("Digite o codigo do funcionario "))
nome = input("Digite o nome do funcionario")
salario = float(input("Digite o salario do funcionario"))
ativo = True

print("Codigo: %d " % codigo)
print("Nome: %s " % nome)
print("Salário: %.2f " % salario)
print("Ativo: %r " % ativo)
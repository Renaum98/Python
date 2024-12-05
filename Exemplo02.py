# É possivel usar mascaras para definir cada tipo de variavel caso necessario como segue os exemplos a seguir

# %d ou %i = Int(inteiro) - Exibe um valor inteiro
# %f = Float ou Double - Exibe um valor decimal
# %Id = Long int - Exibe um numero inteiro longo.
# %e ou %E = Float e double - exibe um numero exponencial
# %c = Char(caractere) - exibe um caractere
# %o = Int - Exibe um numero inteiro em formato octal
# %x ou %X = Int - Exibe um numero inteiro em formato hexadecimal
# %s = Char - Exibe uma cadeia de caracteres
# %r = Boolean - Exibe true ou false

codigo = 105
nome = 'José Santana'
salario = 1500.00
ativo = True

print("Codigo: %d"% codigo)
print("Nome: %s"% nome)
print("Salário: %.2f"% salario)
print("Ativo: %r"% ativo)

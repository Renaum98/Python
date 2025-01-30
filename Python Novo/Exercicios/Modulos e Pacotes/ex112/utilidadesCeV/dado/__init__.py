def leiaDinheiro(valor):
    while valor.isnumeric:
        return valor
    else:
        return f'ERRO, o valor {valor} não é valido'

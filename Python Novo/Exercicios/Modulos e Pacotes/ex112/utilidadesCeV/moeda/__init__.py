def metade(preço,opc=False):
    res = preço / 2
    if opc:
        res = moeda(res)
        return res
    else:
        return res

def dobro(preço, opc = False):
    res = preço * 2
    if opc:
        res = moeda(res)
        return res
    else:
        return res

def diminuir(preço=0, taxa=0, opc = False):
    res = preço - (preço * taxa / 100) 
    if opc:
        res = moeda(res)
        return res
    else: 
        return res

def aumentar(preço=0, taxa=0, opc = False):
    res = preço + (preço * taxa / 100)
    if opc:
        res = moeda(res)
        return res
    else:
        return res


def moeda(txt):
    return f'R${txt:.2f}'

def resumo(preço, taxaAu = 0, taxaDi= 0):
    print('-'*30)
    print('Resumo do Valor'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'Metade do Preço: \t{metade(preço, True)}')
    print(f'{taxaAu}% de aumento: \t{aumentar(preço,taxaAu, True)}')
    print(f'{taxaDi}% de redução: \t{diminuir(preço, taxaDi, True)}')
    print('-'*30)
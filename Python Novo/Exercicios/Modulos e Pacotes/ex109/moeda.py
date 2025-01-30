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



def moeda(txt, opc=False):
    return f'R${txt:.2f}'
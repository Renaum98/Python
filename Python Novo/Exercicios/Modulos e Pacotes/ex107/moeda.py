def metade(preço):
    res = preço / 2
    return res

def dobro(preço):
    res = preço * 2
    return res

def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa / 100) 
    return res

def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa / 100)
    return res
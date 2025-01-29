#Biblioteca de funções para serem usadas em outros programas
def fatorial(n=1):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n=0):
    return n * 2

def triplo(n=0):
    return n * 3
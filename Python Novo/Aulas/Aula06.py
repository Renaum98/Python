#Manipulando cadeias de texto
'''
        Fatiaamento 
    renan
    01234

cada caractere representa um valor que conta de 0 pra frente

para representar um valor escreva
frase = 'João'
print(frase[1]) aqui somente a letra 'o' ira aparecer pois o valor 1 do index em jõao representa a letra 'o'
print(frase[0:2]) aqui ira aparecer desde a letra 'j' até 'o'
print(frase[0:2:2]) aqui ira aparecer desde a letra 'j' até 'o' pulando de 2 em 2
print(frase[:5]) aqui ira começar do inicio até o index 5
print(frase[15:]) aqui ira começar do index 15 e vai até o final da string
print(frase[9::3]) aqui ira começar no index 9 e ir até o final pulando 3 casas de cada vez

'''

frase = 'Um carro de pizza'
print(frase[0::2])

'''
            Analise
    sintaxe - len(frase) 
Exibe o numero de caracteres que uma variavel tem

    sintaxe - frase.count('o',0,13)
Exibe o numero de caracteres 'o' tem na variavel, é possivel tambem usar o fatiamento na sintaxe
    
    sintaxe - frase.find('deo')
Exibe onde esta localizado no index quando começa na variavel o conjunto 'deo'.Se houver alguma string que não foi encontrada, sera exibido o valor -1
'''

'''
        Transformação
    frase.replace('Python','Android')
usado para substituir python por android

    frase.upper()
Usado para colocar todas as letras em maisculos

    frase.lower()
Usado para colocar todas as letras em minusculo

    frase.capitalize()
Usado para colocar a string inteira em minusculo somente deixando a primeira letra em maiusculo

    frase.title()
Usado para colocar todas palavras somente com a primeira letra maiscula de cada uma

    frase.strip()
Usado para apagar os espaçoes excedentes que são colocados no começo ou no final da string
    frase.rstrip()
Tira os espaços da direita
    frase.lstrip()
Tira os espaços da esquerda
'''
'''
        Divisão
    frase.split()
Divide a string e reseta o seu index para cada palavra
exemplo:
        sem split
renan matos
012345678910
        com split
renan matos
01234 01234
ele tambem ira criar uma lista com cada palavra sendo assim:
renan matos
   0    1

        Junção
    '-'.join(frase)
junta todos os elementos da string com um '-' separando as palavras e criando um so index 
'''
'''
        IN
        'palavra' in frase
Verifica se palavra existe na variavel frase
se sim retorna true, se não false
'''
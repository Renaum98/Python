'''FUNÇOES 
Funções são estruturas que possibilitam a separação da programação em blocos.

A implementação de funções em programas é fundamental, pois tem o objetivo de otimizar o código-fonte e evitar a replicação do código, ou seja, definimos as funções uma única vez e sempre que necessário podemos utilizá-las.
SINTAXE:
def nome_da_função (parametros):
    <instruçoes>
return"valor do retorno"
def = a palavra def determina o inicio da função
parametros = são informaçoes que a função pode receber para o seu processamento, os parametros podem existir ou não
corpo da função = É o local em que é aplicada a sequência de instruções, como entrada, processamento e/ou saída.
return = Deve ser utilizado quando houver necessidade de retornar alguma informação para a ação da função.
identação = Deve possuir quatro espaços em branco e pular duas linhas para o próximo bloco de instruções (próxima função ou programação principal).
'''

'''def mensagem1():
    print ('Hello World')


def mensagem2():
    return 'Hello World'


mensagem1()

texto = mensagem2()
print(texto)'''

def lernotas(): #uma função para calcular a media de um aluno
    n=float(input('Digite uma nota para o aluno(a): '))
    return n


def resultado(n1,n2):
    media=(n1+n2)/2
    print('nota1:',n1)
    print('nota2:',n2)
    print('media:',media,'resultado:', end="")
    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')


a = lernotas()
b = lernotas()
resultado(a,b)
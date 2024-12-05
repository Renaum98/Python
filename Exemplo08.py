# Estrutura de decisão
#A estrutura de decisão, também conhecida como estrutura condicional, tem como finalidade comparar e efetuar um desvio de processamento do programa. Caso a condição seja verdadeira, as instruções determinadas após a instrução if serão executadas. Se for necessário executar mais de uma instrução para a condição verdadeira, elas deverão estar escritas dentro de um bloco, ou seja, indentadas corretamente.

# Estrutura simples com if/else
# A estrutura de condição if permite avaliar uma expressão e, se o resultado for verdadeiro, será executada uma determinada ação. Vamos a um exemplo! No código abaixo, temos a verificação da variável idade. Caso o valor da variável seja maior que 18, a condição if é verdadeira, portanto, a mensagem “maior idade” será exibida.

#idade = int(input('Digite a idade da pessoa:'))
#if idade > 18:
    #print('Maior Idade')

a = input('informe um valor pra variavel A:')
b = input('informe um valor pra variavel B:')

if (a>b):
    aux=a;
    a=b;
    b=aux;
print("O valor da variavel A agora é : ", a);
print("O valor da variavel B agora é :", b);


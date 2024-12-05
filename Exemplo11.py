# Estrutura de Repetição
# As estruturas de repetição, também conhecidas como laços de repetição, permitem que um conjunto de instruções seja executado, até que uma determinada condição seja verdadeira.
# são usados o FOR(para) e WHILE(enquanto)

#Normalmente utilizamos a estrutura For quando sabemos quantas vezes o laço de programação deverá ser executado. É a estrutura mais utilizada na linguagem Python. Ela aceita sequências estáticas e geradas por Iteradores. Iteradores são estruturas que permitem acesso a vários itens de uma coleção de elementos, de forma sequencial. Durante a execução de uma estrutura For, o contador aponta para um elemento de uma determinada sequência. A cada iteração, o contador é atualizado para que o laço For processe os elementos correspondentes.

#for n in range(10):
    #print(n)

# No exemplo que acabamos de ver, a variável n é inicialmente ajustada para 0 (inicialização com valor padrão). Uma vez que n é menor do que 10 (condição), o comando print é executado.

# Essa condição é adicionada com o comando range.

# A variável n é incrementada em 1 (incremento padrão) e é testado se o valor de n ainda é menor do que 10.

# O processo se repete até que o valor de n fique maior ou igual a 10.

# Neste instante, o laço termina e o programa segue a execução das instruções do bloco de repetição.

#for n in range(5, 16):
    #print(n)

# Neste caso, os valores apresentados na tela terão como mínimo, o número 5 e, no máximo, 15.

# Utilizar estrutura em ordem decrescente
# Também é possível utilizar o decremento no contador, dentro do comando range.

# for n in range(10, 0, -1):
    #print(n)

# Neste caso, os valores apresentados na tela estarão em ordem decrescente.

# Estrutura While (enquanto)
# A estrutura While (enquanto), executa um determinado conjunto de instruções, enquanto a condição verificada no início permanecer verdadeira.
#Diferente da estrutura For (para), não é necessário determinar o número de vezes que a condição será executada.
#No momento em que a condição for falsa, o processamento da rotina é desviado para fora do laço de repetição.
#Caso a condição seja falsa, logo no início do laço de repetição, as instruções contidas nele são ignoradas.

x = 1;
while x <= 15:
    print(x);
    x=x+1

# É importante observar que, diferente da estrutura For, na estrutura While temos de inicializar a variável antes do início do laço (x=1;) e, também, realizar o incremento dentro do bloco de repetição (x=x+1;).


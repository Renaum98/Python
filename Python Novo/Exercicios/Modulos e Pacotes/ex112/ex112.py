# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
from utilidadesCeV import dado

v = input('Digite um valor: R$')
dado.leiaDinheiro(v)
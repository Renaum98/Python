# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios anteriores para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda
p = float(input('Digite o preço: R$'))
moeda.resumo(p,20,30)
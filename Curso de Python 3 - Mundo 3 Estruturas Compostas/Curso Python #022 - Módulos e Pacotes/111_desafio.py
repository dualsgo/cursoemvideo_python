# Exercício Python #111 - Transformando módulos em pacotes - Aula 00 até 22 - Mundo 3
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadescev import moeda

numero_valido = moeda.obter_valor_numerico('Digite um valor: ')
taxa = moeda.obter_valor_numerico('Digite a taxa: ')

monetario = moeda.perguntar('Em formato monetário? [S/N]: ')
moeda.resumo(numero_valido, taxa, monetario)
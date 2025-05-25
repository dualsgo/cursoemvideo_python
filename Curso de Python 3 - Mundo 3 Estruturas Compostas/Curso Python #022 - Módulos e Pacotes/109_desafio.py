# Exercício Python #109 - Formatando Moedas em Python - Aula 00 até 22 - Mundo 3
# Modifique as funções criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

numero_valido = moeda.obter_valor_numerico('Digite um valor: ')
taxa = moeda.obter_valor_numerico('Digite a taxa: ')
monetario = moeda.perguntar('Em formato monetário? S ou N ')

aumentado = moeda.aumentar(numero_valido, taxa, monetario)
diminuido = moeda.diminuir(numero_valido, taxa, monetario)

dobro = moeda.dobrar(numero_valido, monetario)
metade = moeda.metade(numero_valido, monetario)

print(f"{'Valor:':<15}{numero_valido:>10.2f}")
print(f"{'Aumentado 10%:':<15}{aumentado}")
print(f"{'Diminuído 10%:':<15}{diminuido}")
print(f"{'Dobro:':<15}{dobro}")
print(f"{'Metade:':<15}{metade}")
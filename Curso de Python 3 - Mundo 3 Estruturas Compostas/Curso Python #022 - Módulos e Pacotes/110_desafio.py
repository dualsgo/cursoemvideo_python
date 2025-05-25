# Exercício Python #110 - Reduzindo ainda mais seu programa - Aula 00 até 22 - Mundo 3
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

numero_valido = moeda.obter_valor_inteiro('Digite um valor: ')
taxa = moeda.obter_valor_inteiro('Digite a taxa: ')
monetario = moeda.perguntar('Em formato monetário? S ou N ')
moeda.resumo(numero_valido, taxa, monetario)
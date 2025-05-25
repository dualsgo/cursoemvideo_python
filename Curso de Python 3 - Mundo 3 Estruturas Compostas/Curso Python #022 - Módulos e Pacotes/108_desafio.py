# Exercício Python #108 - Formatando Moedas em Python - Aula 00 até 21 - Mundo 3
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


# Arquivo principal.py

import moeda

valor = moeda.obter_valor_numerico('Digite um valor: ')
taxa = moeda.obter_valor_numerico('Digite a taxa: ')
resposta = moeda.perguntar('Deseja formatar os valores como moeda? [S/N]: ')

moeda.resumo(valor, taxa, resposta)


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, temos que adaptar o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

# A função moeda() deve receber um valor e retornar o valor formatado como moeda.

def formato_monetario(valor):
    # Vamos formatar o valor como moeda. O método f'{valor:,.2f}' vai formatar o valor com duas casas decimais e separador de milhar. O método replace() vai substituir o ponto por vírgula e a vírgula por ponto. O parâmetro 1 no final do método replace() vai garantir que apenas a primeira vírgula seja substituída.
	return f'R${valor:,.2f}'.replace('.', ',').replace(',', '.', 1)


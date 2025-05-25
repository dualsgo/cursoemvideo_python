# Exercício Python #036 - Aprovando Empréstimo - Aula 00 até 12 - Mundo 2
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

# Tarefa 1: Perguntar o valor da casa, o salário do comprador e em quantos anos vai pagar
valor_imovel = int(input('Digite o valor do imóvel: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos_pagando = int(input('Digite a quantidade de anos que deseja pagar: '))

# Tarefa 2: Verificar se a prestação mensal é maior que 30% do salário
limite = salario * .3
prestacoes = anos_pagando * 12
valor_prestacoes = valor_imovel / prestacoes

if valor_prestacoes >= limite:
    print('\033[1;31mNão será possível aprovar o seu empréstimo. O valor das prestações é superior ao limite de 30% do seu salário.\033[m')
    print(f'Valor das prestações: \033[1;31mR$ {valor_prestacoes:.2f}\033[m')
else:
    print('\033[1;32mParabéns! Seu empréstimo foi aprovado. Confira as condições:\033[m')
# Tarefa 3: Após a verificação, mostrar se o empréstimo foi aprovado ou negado.
    print(f'O imóvel avaliado em \033[1;32mR$ {valor_imovel:.2f}\033[m será quitado em \033[1;32m{anos_pagando}\033[m anos.')
    print(f'Cada uma das \033[1;32m{prestacoes}\033[m parcelas custará \033[1;32mR$ {valor_prestacoes:.2f}\033[m')
    
# Versão 2 - Sem validação
try:
	valor_imovel = float(input('Digite o valor do imóvel: R$'))
	renda = float(input('Digite o valor do salário: R$'))
	prazo_anos = int(input('Prazo em anos: '))
	anos_meses = prazo_anos * 12
	parcelas = valor_imovel / anos_meses
	limite = renda * .3
	verifica = limite >= parcelas

	if verifica:
		print(f'Aprovado')
		print(f'{'Valor imóvel:':<15}{'R$':>5}{valor_imovel:>10.2f}')
		print(f'{'Prazo (meses):':<15}{anos_meses:>9}{' meses':>6}')
		print(f'{'Valor parcelas:':<15}{'R$':>5}{parcelas:>10.2f}')
	else:
		print(f'Recusado')

except ValueError:
	print('Valores inválidos para essa operação.')

# versão 3 - Mais completa
def obter_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Valor inválido para essa operação. Digite novamente.')


def verificação(v, s, p):
    parcela = v / p
    parcela_máxima = s * .3
    consulta = True if parcela <= parcela_máxima else False

    print(
        f'{'Valor do imóvel:':<20}{f'R$ {v:.2f}':>15}\n'
        f'{'Salário:':<20}{f'R$ {s:.2f}':>15}\n'
        f'{'Prazo em anos:':<20}{f'{p/12:.1g} anos':>15}\n'
        f'{'-' * 35}\n'
        f'{'Parcelas:':<20}{prazo:>15}\n'
        f'{'Parcela máxima:':<20}{f'R$ {parcela_máxima:.2f}':>15}\n'
        f'{'Parcela simulada:':<20}{f'R$ {parcela:.2f}':>15}\n'
        f'{'-' * 35}\n'
        f'{'Resultado:':<20}{'APROVADO' if consulta else 'NEGADO':>15}\n')


valor_casa = obter_valor('Digite o valor da casa: R$ ')
salário = obter_valor('Digite o valor do salário: R$ ')
prazo = int(obter_valor('Prazo em anos: ')) * 12
verificação(valor_casa, salário, prazo)

# EXTRA - Cálculo de parcelas

s = 100000.  # Saldo devedor inicial
entrada = 0  # Valor da entrada inicial (se houver)
n = 100  # Número total de parcelas
m = 0  # Número de parcelas já pagas
taxa_juros_anual = 0.08  # Taxa de juros anual (8% ao ano)

# Convertendo a taxa de juros anual para mensal
taxa_juros_mensal = taxa_juros_anual / 12

# Se houver uma entrada, subtraí-la do saldo devedor inicial
s -= entrada
juros = taxa_juros_mensal

for i in range(1, n+1):
    p = (taxa_juros_mensal * s) / (1 - (1 + taxa_juros_mensal)**(-n))
    m += 1
    amortizacao = p - juros
    juros = s * taxa_juros_mensal
    print(f'Parcela {i}: R$ {p:.2f} (Amortização: R$ {amortizacao:.2f}, Juros: R$ {juros:.2f}, Saldo Devedor: R$ {s:.2f})')
    s -= p
    
# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa deve aprovar ou negar um empréstimo bancário para a compra de uma casa. Para isso, o programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# A primeira coisa a ser feita é perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Para isso, vamos utilizar a função input() para ler os valores e a função float() para converter o valor da casa para ponto flutuante e a função int() para converter a quantidade de anos para inteiro.
valor_imovel = float(input('Digite o valor do imóvel: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos_pagando = int(input('Digite a quantidade de anos que deseja pagar: '))

# Em seguida, vamos verificar se a prestação mensal é maior que 30% do salário. Para isso, vamos calcular o valor da prestação mensal dividindo o valor do imóvel pela quantidade de meses que o comprador vai pagar. Em seguida, vamos calcular o limite de 30% do salário e verificar se o valor da prestação é maior ou igual ao limite.

# Antes, vamos converter a quantidade de anos para meses multiplicando por 12.
prestacoes = anos_pagando * 12

# Agora, vamos calcular o valor da prestação mensal e o limite de 30% do salário.
valor_prestacoes = valor_imovel / prestacoes
limite = salario * .3

# Por fim, vamos verificar se o valor da prestação é maior ou igual ao limite de 30% do salário e exibir uma mensagem informando se o empréstimo foi aprovado ou negado.

if valor_prestacoes >= limite:
    print(f'Com um salário de R$ {salario:.2f}, não será possível aprovar o seu empréstimo. O valor das prestações é superior ao limite de 30% do seu salário.')
    print(f'Limites: R$ {limite:.2f}')
    print(f'Valor das prestações: R$ {valor_prestacoes:.2f}')
else:
    print('Parabéns! Seu empréstimo foi aprovado. Confira as condições:')
    print(f'O imóvel avaliado em R$ {valor_imovel:.2f} será quitado em {anos_pagando} anos.')
    print(f'Cada uma das {prestacoes} parcelas custará R$ {valor_prestacoes:.2f}')
# Exercício Python #071 - Simulador de Caixa Eletrônico - Aula 00 até 15 - Mundo 2
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


from emoji import emojize

# Mensagem de boas-vindas
print(emojize(':banco::moeda: BANCO GUANABARA :moeda::banco:', language='pt'))

while True:
    try:
        # Solicita ao usuário o valor desejado para saque
        valor_saque = int(input(emojize(':símbolo_de_caixa_automático: Quanto deseja sacar? R$ ', language='pt')))
        break
    except ValueError:
        print('Valor inválido!')

# Variável para armazenar a quantidade de cédulas
cedulas = 0

# Loop para calcular as cédulas necessárias
while True:
    if valor_saque >= 100:
        cedulas = valor_saque // 100
        valor_saque %= 100
        print(emojize(f'{f':nota_de_dólar: Sacando {cedulas} cédulas de R$ ':<30}{'100':>3}', language='pt'))

    elif valor_saque >= 50:
        cedulas = valor_saque // 50
        valor_saque %= 50
        print(emojize(f'{f':nota_de_dólar: Sacando {cedulas} {'cédulas' if cedulas > 1 else 'cédula '} de R$ ':<30}{'50':>3}', language='pt'))

    elif valor_saque >= 20:
        cedulas = valor_saque // 20
        valor_saque %= 20
        print(emojize(f'{f':nota_de_dólar: Sacando {cedulas} {'cédulas' if cedulas > 1 else 'cédula '} de R$ ':<30}{'20':>3}', language='pt'))

    elif valor_saque >= 10:
        cedulas = valor_saque // 10
        valor_saque %= 10
        print(emojize(f'{f':nota_de_dólar: Sacando {cedulas} {'cédulas' if cedulas > 1 else 'cédula '} de R$ ':<30}{'10':>3}', language='pt'))

    elif valor_saque >= 5:
        cedulas = valor_saque // 5
        valor_saque %= 5
        print(emojize(f'{f':nota_de_dólar: Sacando {cedulas} {'cédulas' if cedulas > 1 else 'cédula '} de R$ ':<30}{'5':>3}', language='pt'))

    elif valor_saque >= 2:
        cedulas = valor_saque // 2
        valor_saque %= 2
        print(emojize(f'{f':nota_de_dólar: Sacando {cedulas} {'cédulas' if cedulas > 1 else 'cédula '} de R$ ':<30}{'2':>3}', language='pt'))

    else:
        # Quando não há mais cédulas a serem sacadas, encerra o loop
        print(emojize(':rosto_com_cifrões: RETIRE O SEU DINHEIRO', language='pt'))
        break

# Mensagem de agradecimento ao usuário por utilizar os serviços do banco
print(emojize('Obrigado por utilizar os nossos serviços!', language='pt'))

# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, vamos criar um programa que simule o funcionamento de um caixa eletrônico. No início, o programa deve perguntar ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# Vamos iniciar a variável cedulas com 0 para armazenar a quantidade de cédulas.
cedulas = 0

# Vamos pergunta ao usuário o valor desejado para saque.
valor_saque = int(input('Quanto deseja sacar? R$ '))

# Vamos criar um loop para calcular as cédulas necessárias.
while True:
    if valor_saque >= 100:
        cedulas = valor_saque // 100
        valor_saque %= 100
        print(f'Sacando {cedulas} cédulas de R$ 100')

    elif valor_saque >= 50:
        cedulas = valor_saque // 50
        valor_saque %= 50
        print(f'Sacando {cedulas} cédulas de R$ 50')

    elif valor_saque >= 20:
        cedulas = valor_saque // 20
        valor_saque %= 20
        print(f'Sacando {cedulas} cédulas de R$ 20')

    elif valor_saque >= 10:
        cedulas = valor_saque // 10
        valor_saque %= 10
        print(f'Sacando {cedulas} cédulas de R$ 10')

    elif valor_saque >= 5:
        cedulas = valor_saque // 5
        valor_saque %= 5
        print(f'Sacando {cedulas} cédulas de R$ 5')

    elif valor_saque >= 2:
        cedulas = valor_saque // 2
        valor_saque %= 2
        print(f'Sacando {cedulas} cédulas de R$ 2')

    else:
        # Quando não há mais cédulas a serem sacadas, encerra o loop
        print('RETIRE O SEU DINHEIRO')
        break
    
# Essa estrutura pode ser simplificada com o uso de listas e laços de repetição. Veja o exemplo abaixo:
valor_saque = int(input('Quanto deseja sacar? R$ ')) # Solicita ao usuário o valor desejado para saque

for cedula in [100, 50, 20, 10, 5, 2]: # Percorre a lista de cédulas disponíveis
    quantidade = valor_saque // cedula # Calcula a quantidade de cédulas necessárias para o valor de saque atual e a cédula atual
    valor_saque %= cedula # Atualiza o valor de saque subtraindo o valor das cédulas já sacadas
    
    if quantidade > 0: # Verifica se a quantidade de cédulas é maior que zero
        print(f'Sacando {quantidade} cédula(s) de R$ {cedula}') # Exibe a quantidade de cédulas a ser sacada
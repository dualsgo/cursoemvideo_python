# Exercício Python #043 - Índice de Massa Corporal - Aula 00 até 12 - Mundo 2
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre sua posição, conforme a tabela abaixo:

# O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em m), conforme a seguinte fórmula: IMC = peso / (altura x altura). O resultado de IMC é dado em kg/m 2.

# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

# Tarefa 1: Receber o peso e a altura para calcular o imc
peso = float(input('Digite seu peso: Kg'))
altura = float(input('Digite sua altura em metros: m'))


# Tarefa 2: Formar a tabela com as condições para categorizar o imc
imc = peso / (altura * altura)
print(f'Seu IMC é {imc:.1f}.', end= ' ')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
# Tarefa 3: Exibir o resultado

# SIMPLIFICADA 
try:
	peso_kg = float(input('Peso em Kg: '))
	altura_metros = float(input('Altura em metros: '))
	imc = round(peso_kg / (altura_metros * altura_metros), 2)
	categoria = 'Abaixo do peso' if imc < 18.5 else 'Peso ideal' if imc < 25 else 'Sobrepeso' if imc < 30 else 'Obesidade' if imc < 40 else 'Obesidade mórbida'
	print('-' * 55)
	print(f'|{'Peso (Kg)':^10}|{'Altura (m)':^10}|{'IMC':^10}|{'Categoria':^20}|')
	print('-' * 55)
	print(f'|{peso_kg:^10}|{altura_metros:^10.2f}|{imc:^10}|{categoria:^20}|')
	print('-' * 55)
except ValueError:
	print(f'Erro! Valores inválidos para essa operação.')


# VERSÃO COMPLETA

def obter_valor(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Tipo de dado inválido.')

peso = obter_valor('Digite o peso em Kg: ')
while 0 > peso or peso > 200:
    print('Peso inválido!')
    peso = obter_valor('Digite o peso em Kg: ')

altura = obter_valor('Digite a altura em cm: ')
while 0 > altura or altura > 300:
    print('Altura inválida!')
    altura = obter_valor('Digite a altura em cm: ')

if altura >= 100:
    altura = altura / 100

imc = round(peso / (altura * altura), 2)

categoria = (
    'Abaixo do peso' if imc < 18.5 else
    'Peso ideal' if imc < 25 else
    'Sobrepeso' if imc < 30 else
    'Obesidade' if imc < 40 else
    'Obesidade mórbida'
)

print(f'{"Peso:":<10}{f"{peso:.2f} Kg":>20}')
print(f'{"Altura:":<10}{f"{altura:.2f} m":>20}')
print(f'{"IMC:":<10}{imc:>20}')
print('-' * 30)
print(f'{"Categoria:":<10}{categoria:>20}')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, aprendemos a criar um programa que calcula o IMC de uma pessoa e exibe a categoria do IMC de acordo com a tabela fornecida no enunciado. Para isso, utilizamos a fórmula do IMC, que é o peso dividido pela altura ao quadrado, e criamos uma estrutura condicional para verificar em qual categoria o IMC se encaixa.

# A primeira coisa a ser feita é ler o peso e a altura da pessoa. Para isso, utilizamos a função input() para ler os valores e a função float() para converter os valores para ponto flutuante.
peso = float(input('Digite seu peso: Kg'))
altura = float(input('Digite sua altura em metros: m'))

# Em seguida, calculamos o IMC da pessoa utilizando a fórmula IMC = peso / (altura x altura).
imc = peso / (altura * altura)
print(f'Seu IMC é {imc:.1f}.', end=' ')

# Por fim, utilizamos uma estrutura condicional para verificar em qual categoria o IMC se encaixa e exibimos a categoria correspondente.
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

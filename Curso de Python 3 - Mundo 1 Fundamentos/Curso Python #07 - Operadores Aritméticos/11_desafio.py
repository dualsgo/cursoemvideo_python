# Exercício Python #011 - Pintando Parede - Aula 00 até 07 - Mundo 1
# Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2m².

def medida(mensagem):
	while True:
		try:
			return float(input(mensagem))
		except ValueError:
			print('O valor fornecido não é válido para essa operação.')

largura = medida('Largura: ')
altura = medida('Altura: ')
metro_quadrado = largura * altura
rendimento = metro_quadrado / 2

print(f'''
{'Largura:':<10}{largura:>5.2f}m
{'Altura:':<10}{altura:>5.2f}m
{'-' * 16}
{'Metro²':<10}{metro_quadrado:>5.2f}
{'Tinta:'}{rendimento:>6.1f}L''')


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa solicita ao usuário a largura e a altura de uma parede em metros e calcula a quantidade de tinta necessária para pintá-la. A área da parede é calculada multiplicando a largura pela altura. A quantidade de tinta necessária é obtida dividindo a área da parede por 2, que é o rendimento de um litro de tinta.

# Primeiro salvamos a largura e a altura da parede em variáveis. Utilizamos a função input() para solicitar os valores ao usuário e a função float() para converter os valores em números de ponto flutuante.
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

# A área da parede é calculada multiplicando a largura pela altura. O resultado é armazenado na variável area.
area = largura * altura

# O rendimento da tinta é de 2m² por litro. Para calcular a quantidade de tinta necessária, dividimos a área da parede por 2. O resultado é armazenado na variável tinta.
tinta = area / 2

# Agora exibimos a largura, a altura, a área da parede e a quantidade de tinta necessária na tela.
print(f'Largura: {largura:.2f}m')
print(f'Altura: {altura:.2f}m')
print(f'Área: {area:.2f}m²')
print(f'Tinta necessária: {tinta:.2f} litros')

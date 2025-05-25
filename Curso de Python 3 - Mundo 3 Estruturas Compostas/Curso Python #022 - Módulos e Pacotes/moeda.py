# Exercício Python #107 - Exercitando módulos em Python - Aula 00 até 22 - Mundo 3
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Arquivo moeda.py

def obter_valor_numerico(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Valor inválido para essa operação.')

def perguntar(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in 'SN':
            return resposta == 'S'

def aumentar(valor, porcentagem, formatar=False):
    resultado = valor + (valor * (porcentagem / 100))
    return formato_monetario(resultado) if formatar else resultado

def diminuir(valor, porcentagem, formatar=False):
    resultado = valor - (valor * (porcentagem / 100))
    return formato_monetario(resultado) if formatar else resultado

def dobrar(valor, formatar=False):
    resultado = valor * 2
    return formato_monetario(resultado) if formatar else resultado

def metade(valor, formatar=False):
    resultado = valor / 2
    return formato_monetario(resultado) if formatar else resultado

def formato_monetario(valor):
    return f'R${valor:,.2f}'.replace('.', ',').replace(',', '.', 1)

def resumo(valor, taxa, resposta):
    print(f"{'Valor:':<15}{formato_monetario(valor)}")
    print(f"{'Aumentado 10%:':<15}{aumentar(valor, taxa, resposta)}")
    print(f"{'Diminuído 10%:':<15}{diminuir(valor, taxa, resposta)}")
    print(f"{'Dobro:':<15}{dobrar(valor, resposta)}")
    print(f"{'Metade:':<15}{metade(valor, resposta)}")
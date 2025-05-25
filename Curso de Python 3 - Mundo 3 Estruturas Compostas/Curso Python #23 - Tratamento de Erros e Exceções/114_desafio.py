# Exercício Python #114 - Site está acessível? - Aula 00 até 23 - Mundo 3
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests


def verifica_disponibilidade(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f'O site {url} está disponível.')
        else:
            print(f'O site {url} retornou um código de resposta diferente de 200: {response.status_code}')

    except requests.ConnectionError:
        print(f'Erro de conexão: Não foi possível conectar ao site {url}.')
    except requests.RequestException as e:
        print(f'Erro na requisição: {e}')

site = input('Digite o site que deseja verificar: ').strip()
verifica_disponibilidade(f'https://www.{site}.com.br')
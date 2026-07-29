
# Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.

class Livro():

    def __init__(self, quantidade_paginas):
        self.paginas = quantidade_paginas


    def leitura(self):
        pagina_atual = 1
        while self.paginas >= pagina_atual:
            print(f'\nPágina {pagina_atual}')
            print(f'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui diam, sodales in imperdiet ut, sollicitudin sit amet')
            print(f'Lido: {(pagina_atual/self.paginas)*100:.2f}%')
            pagina_atual += 1

teste = Livro(3)
teste.leitura()
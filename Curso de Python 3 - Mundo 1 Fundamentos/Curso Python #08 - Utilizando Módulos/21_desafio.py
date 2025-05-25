# Exercício Python #021 - Tocando um MP3 - Aulas 00 até 08 - Mundo 1
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
from emoji import emojize
arquivo = r'C:\Users\mdbsi\OneDrive\Área de Trabalho\meus-estudos\cursoemvideo_python\Curso de Python 3 - Mundo 1 Fundamentos\Curso Python #08 - Utilizando Módulos\audio.mp3'

pygame.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
pygame.event.wait()

print(emojize(':notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais::notas_musicais:', language='pt'))
input("Pressione Enter para sair...")  # Mantém o programa em execução até que Enter seja pressionado


# Estou compartilhando minhas anotações sobre os exercícios. Quem quiser, pode copiar e colar em um documento .py pois está tudo formatado e comentado.

# Nesse exercício, o programa utiliza a biblioteca pygame para abrir e reproduzir um arquivo de áudio MP3. A biblioteca pygame é uma biblioteca de jogos que também pode ser utilizada para reproduzir arquivos de áudio.

# Primeiro, importamos a biblioteca pygame.
import pygame

# Se em seu PyCharm não funcionar o pygame, instale o pacote pygame no terminal do PyCharm com o comando pip install pygame.
# Outra opção é clicar no ícone de configurações do PyCharm, ir em Project: nome_do_projeto > Python Interpreter e clicar no botão + para adicionar o pacote pygame.
# Ou clicar no ícone de lâmpada que aparece ao lado do import pygame e clicar em Install package 'pygame'.

# Em seguida, carregamos o arquivo de áudio MP3 utilizando a função pygame.mixer.music.load(). O caminho do arquivo é passado como argumento para a função.

# NOTA: O caminho do arquivo de áudio deve ser passado como uma string. Caso o arquivo esteja em um diretório diferente do arquivo Python, é necessário informar o caminho completo do arquivo.
# Para saber o caminho do arquivo, clique com o botão direito sobre o arquivo e selecione Propriedades. Na janela que abrir, copie o caminho que aparece em Localização.

# Para facilitar, vamos salvar o caminho do arquivo em uma variável chamada arquivo.
arquivo = 'Cole o caminho do arquivo de áudio MP3 aqui'

# NOTA: Geralmente, o caminho de um arquivo no Windows começa com C:\, seguido do nome do usuário, como C:\Users\NomeDoUsuario\. Note que a barra invertida (\) é utilizada para separar pastas no Windows. No Python, a barra invertida é um caractere de escape, então é necessário utilizar duas barras invertidas (\\) para representar uma barra invertida caso contrário, o Python interpretará a barra invertida como um caractere de escape e isso pode gerar um erro.

# Outra opção é substituir a barra invertida por uma barra normal (/) ou utilizar uma string de caminho cru (raw string) adicionando um r antes da string. Por exemplo, r'C:\Users\NomeDoUsuario\Arquivo.mp3'.  # O r antes da string indica que é uma string de caminho cru.

# Feito isso vamos seguir com o código.

# Inicializamos o módulo pygame com a função pygame.init(). Essa função é necessária para inicializar todos os módulos do pygame.
pygame.init()

# Carregamos o arquivo de áudio MP3 utilizando a função pygame.mixer.music.load(). O caminho do arquivo é passado como argumento para a função.
pygame.mixer.music.load(arquivo)

# Reproduzimos o arquivo de áudio MP3 utilizando a função pygame.mixer.music.play(). Essa função inicia a reprodução do arquivo de áudio.
pygame.mixer.music.play()

# A função pygame.event.wait() é utilizada para manter o programa em execução até que a reprodução do arquivo de áudio seja concluída. Essa função aguarda a finalização da reprodução do arquivo de áudio antes de continuar a execução do programa.
pygame.event.wait()

# Por fim, exibimos uma mensagem na tela para informar ao usuário que o arquivo de áudio está sendo reproduzido. A função input() é utilizada para manter o programa em execução até que o usuário pressione Enter. Dessa forma, o programa não será encerrado imediatamente após a reprodução do arquivo de áudio.
print('Reproduzindo o arquivo de áudio...')
input('Pressione Enter para sair...')
# O programa será encerrado após o usuário pressionar Enter.
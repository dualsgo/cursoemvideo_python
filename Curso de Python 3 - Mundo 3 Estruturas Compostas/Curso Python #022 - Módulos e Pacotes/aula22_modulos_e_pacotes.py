# Curso Python #22 - Módulos e Pacotes

# Modularizar é o ato de construir módulos.
# É um conceito que surgiu nos anos 60 quando os programas se tornaram cada vez maiores e isso dificultava a leitura e manutenção dos códigos. Dividindo o programa a legibilidade melhora e facilita a manutenção.

# Python recomenda que a sintaxe de importação seja o módulo inteiro. Importar apenas funções de um módulo pode gerar conflitos

from uteis import numeros
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobrar(fat)}')
print(f'O triplo de {num} é {numeros.triplicar(fat)}')


# Vantagens:
# Organização
# Facilidade na manutenção
# Ocultação do código detalhado
# Reutilização das funções em outros projetos

# Pacotes (Bibliotecas, libs)

# Pacotes podem conter muitos módulos caso os módulos fiquem grandes, precisamos criar vários módulos.

# Podemos separar por assuntos. Dentro do pacote podemos ter módulos específicos para tratar números, por exemplo.

# Assim como  antes, podemos importar tanto o pacote inteiro, com todos os módulos ou apenas módulos específicos do pacote

# import pacote_uteis
# from pacote_uteis import modulo_numeros

# Para criar um pacote, criamos uma pasta dentro do projeto onde os módulos (arquivos .py contendo as funções) estarão


#      [ ] PACOTE_UTEIS
#       |
#       |------ [] CORES
#       |
#       |------ [] DATAS
#       |
#       |------ [] NUMEROS
#       |
#       |------ [] STRINGS

# Dentro de cada pasta é necessário haver um arquivo __init__.py
# Curso Python #11 - Cores no Terminal
# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# Padrão ANSI - escape sequence: Utilizaremos contra barra \

# Cores, sintaxe com a faixa 033
# \033[style;text;backgroundm

print('\033[0;33;44m Texto')
# A ordem é opcional, pois cada faixa de código corresponde a um padrão específico

# STYLE: 0 - None, 1 - Bold, 4 - Underline, 7 - Negative
# TEXT: 30 - Branco (padrão), 31 - Vermelho, 32 - Verde, 33 - Amarelo, 34 - Azul, 35 - Roxo, 36 - Azul-claro, 37 - Cinza
# BACKGROUND: 40 - Branco (padrão), 41 - Vermelho, 42 - Verde, 43 - Amarelo, 44 - Azul, 45 - Roxo, 46 - Azul-claro, 47 -




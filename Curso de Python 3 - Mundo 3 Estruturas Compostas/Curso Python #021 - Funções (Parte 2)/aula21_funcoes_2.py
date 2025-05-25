# Curso Python #21 - Funções (Parte 2)
# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.

# Interactive Help - usamos a função help() para obter a documentação
# help(input)
# print(input.__doc__)

# docstrings - São strings com a documentação da função criada

def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: INÍCIO da contagem
    :param f: FIM da contagem
    :param p: PASSO daa contagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


# help(contador)

# Parâmetros opcionais - Atribui um valor padrão a um ou mais parâmetros caso não seja passado um valor pelo usuário. É usado para um número pré-definido de parâmetros. Caso seja um número desconhecido utilizar o desempacotamento
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')


# somar(c=3)

# Escopo de variáveis
def teste(b):
    # global a - este comando trataria a como escopo global. A declaração abaixo atualizaria o valor original de 5 para 8
    a = 8  # "a" dentro possui escopo local
    b += 4  # "b" possui escopo local, recebe o valor original de "a" e incrementa 4
    c = 2  # "c" possui escopo local
    print(f'a local vale {a}.')
    print(f'b local vale {b}.')
    print(f'c local vale {c}.')


# Programa principal
a = 5
teste(a)  # O parâmetro b recebe o valor de a
print(f'a global vale {a}.')  # "a" fora tem escopo global e vale seu valor original
# print(f'B dentro vale {b}.')  Apesentaria erro devido ao escopo local
# print(f'C dentro vale {c}.')  Apesentaria erro devido ao escopo local


# Retorno de valores - Usamos a palavra chave return

def soma_valores(pri=0, seg=0, ter=0):
    sv = pri + seg + ter
    # print(f'A soma vale {sv}.')
    return sv  # Com return, o resultado é retornado e pode ser manipulado separadamente

"""soma_valores(2, 5, 7)
soma_valores(7, 8)
soma_valores(9)
# Nessa versão cada resultado é exibido separadamente com print()"""

print(f'A somas valem {soma_valores(2, 5, 7)}, {soma_valores(7, 8)} e {soma_valores(9)}.')
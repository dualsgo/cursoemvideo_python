# Você sabe como funciona uma variável simples. Relembrando...

estado = 'SP'
# E se quiser armazenar mais de um estado?
estado = 'RJ'
# Se fizermos uma nova atrivuição, o valor anterior é perdido.

# Surgiram as variáveis compostas.
estados = ['RJ', 'SP', 'CE']
#            0    1     2

# Cada estado é armazenado em uma posição, ou índice, dentro da variável composta.

# Se quisermos acessar um estado específico, basta usar o índice.
print(estados[2])  # CE

# Se quiser adicionar algum estado em um determinado indice, o valor anterior é perdido.
estados[1] = 'RJ'

# As listas ainda tem alguns inconvenientes, como a necessidade de usar índices para acessar os estados, o que pode ser confuso e propenso a erros. Para isso foram criados os dicionários, que permitem armazenar os estados com chaves mais significativas.

aluno = {'nome': 'João', 'turma': 301, 'nota': 8.5, 'ativo': True}

# Podemos acessar os valores usando as chaves, que são mais intuitivas do que os índices.
print(aluno['nome'])  # João

# O maior problema é a separação entre dados e funções. O dicionário é apenas um recipiente de dados, e as funções que operam sobre esses dados estão separadas.

# O ideal seria permitir que a variável execute funcionalidades internas. Foi aí que surgiu o conceito de objetos.

# Assim, um objeto é uma variavel que além de guardar dados, pode executar uma função. Em outras palavras, objetos são variáveis qeu além de guardar dados, podem fazer coisas com esses dados.

# Declaração básica:
  # Regras para nomear uma classe:
    # 1. O nome da classe deve começar com letra maiúscula.
    # 2. O nome da classe deve ser escrito em CamelCase, ou seja, cada palavra deve começar com letra maiúscula e não deve conter espaços ou caracteres especiais.

# class MinhaClasse:
    # Atributo de classe
    # Método de classe

# Declaração de um objeto a partir da classe
# obj = MinhaClasse()

# Os parênteses indicam uma instanciação da classe, ou seja, a criação de um objeto a partir da classe. 
# Dentro dos parênteses, podemos passar argumentos para o método construtor da classe, que é um método especial responsável por inicializar os atributos do objeto. Se a classe não tiver um método construtor definido, os parênteses podem ser deixados vazios.

# Método construtor def __init__(self):

class Gafanhoto:
    # Método construtor
    def __init__(self):
        # Atributos de instância
        self.nome = ''
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhnoto(a) e tem {self.idade} anos de idade.'

# Declaração de objeto

objeto = Gafanhoto()
objeto.nome = 'Maycon'
objeto.idade = 32
objeto.aniversario()
print(objeto.mensagem())

objeto2 = Gafanhoto()
objeto2.nome = 'Mauro'
objeto2.idade = 52
print(objeto2.mensagem())
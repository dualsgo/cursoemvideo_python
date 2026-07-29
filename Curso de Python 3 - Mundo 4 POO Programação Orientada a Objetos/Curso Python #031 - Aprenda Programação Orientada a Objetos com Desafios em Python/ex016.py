# Crie a Classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permite ao funcionário se apresentar

class Funcionario():

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f'Colaborador: {self.nome}\nSetor: {self.setor}\nCargo: {self.cargo}'


colaborador = Funcionario('Maycon', 'Loja', 'Líder da Diversão')
print(colaborador.apresentar())
colaborador = Funcionario('Bartolomeu', 'Escritório', 'Analista')
print(colaborador.apresentar())
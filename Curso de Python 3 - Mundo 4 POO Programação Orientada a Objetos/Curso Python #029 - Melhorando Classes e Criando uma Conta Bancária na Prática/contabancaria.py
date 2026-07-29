class ContaBancaria():  
    """
    Cria uma conta bancária e permite realizar operações como saque e depósito.
    """
    def __init__(self, id, nome, saldo =0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(f'Conta {self.id} criado com sucesso. Saldo atual: R$ {self.saldo:.2f}')
        
    def __str__(self):
        return f'A conta {self.id} pertence a {self.nome} e tem saldo de R${self.saldo:.2f}'

    def depositar(self, valor):
        print(f'Depósito de {valor:.2f} realizado na conta {self.id}')
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            print(f'O saldo atual é inferior ao valor do saque!\nSaldo: R$ {self.saldo}')
        else:
            print(f'Saque de R$ {valor:.2f} realizado na conta {self.id}')
            self.saldo -= valor


conta1 = ContaBancaria(12345, 'Maycon', 100)
print(conta1)
conta1.depositar(100)
print(conta1)
conta1.sacar(199)
print(conta1)
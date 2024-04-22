from abc import ABC, abstractmethod, abstractproperty, property
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_fisica(Cliente):
    def __init__(self, nome, data_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

        @classmethod
        def nova_conta(cls, cliente, numero):
            return cls(numero, cliente)
        @property
        def saldo(self):
            return self._saldo
        @property
        def numero(self):
            return self._numero

        @property
        def agencia(self):
            return self._agencia
        
        @property
        def client(self):
            return self._cliente
        
        @property
        def Historico(self):
            return self._historico

        def sacar(self, valor):
            saldo = self.saldo
            exced_saldo = valor > saldo

            if exced_saldo:
                print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            elif valor > 0:
                self.saldo -= valor
                print("\n=== Saque realizado com suceesso! ===")
                return True
            else:
                print("\n@@@ Operação falou! Valor inválido! @@@")

            return False
        
        def depositar(self, valor):
            if valor > 0:
                self._saldo += valor
                print("\n=== Depósito realizado com sucesso! ===")
            else:
                print("\n@@@ Operação falhou! Valor inválido. @@@")
                return False

            return True
        
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

        def sacar(self, valor):
            numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

            excedeu_limite = valor > self.limite
            excedeu_saques = numero_saques >= self.limite_saques

            if excedeu_limite:
                print("\n@@@ Operação falhou! Valor do saque excedeu o limite. @@@")
            elif excedeu_saques:
                print("\n@@@ Operação falhou! Limite de saques atingido. @@@")
            else:
                return super().sacar(valor)
            
            return False
        
def __str__(self):
    return f"""\
        Agência:\t{self.agencia}
        C/c:\t\t{self.numero}
        Titular:\t{self:cliente.nome}
    """

class Historico:
    def __init__(self):
        self.transacao = []
    
    @property
    def transacao(self):
        return self.transacao
    
    def adicionar_transacao(self, transacao):
        self.transacao.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass            

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            
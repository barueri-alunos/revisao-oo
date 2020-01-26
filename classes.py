from random import randint


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente):
        self.titular = cliente
        self.numero = self._gerar()
        self.saldo = 0

    def extrato(self):
        print(f'Numero da conta: {self.numero}\nSaldo: {self.saldo}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def consultar_saldo(self):
        return self.saldo

    def _gerar(self):
        self.random_numero = f'{randint(1000, 9999)}-{randint(1, 9)}'
        return self.random_numero



17. Crie uma classe ContaBancaria com titular, saldo, historico e os métodos depositar, sacar, transferir e extrato.
R:
class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"+R$ {valor:.2f}")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"-R$ {valor:.2f}")
          return True
        return False

    def transferir(self, valor, destino):
        if self.sacar(valor):
            destino.depositar(valor)

    def extrato(self):
        print(self.titular, self.historico, f"Saldo: R$ {self.saldo:.2f}")

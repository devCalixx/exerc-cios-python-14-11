class conta_bancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        self.__saldo += valor
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    def exibir_saldo(self):
        print(f"Saldo: {self.__saldo}")

conta = conta_bancaria("João", 1000)
conta.depositar(500)
conta.sacar(800)
conta.exibir_saldo()
conta.sacar(2000)
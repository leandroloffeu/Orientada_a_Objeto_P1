class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self. saldo = saldo
        self. limite = limite

    def Exibir(self):
        print(f' Número da Conta: {self.numero} \n O nome do titular: {self.titular}\n Saldo da Conta: {self.saldo}\n Limite: {self.limite}')

    def deposita(self,valor):        
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >=  valor:
            self.saldo -= valor
            print (f'Saldo de R$ {self.saldo}')
        else:
            print(f'saldo insuficiente {self.saldo}')
            
    def  extrato(self):
        print(f'O Saldo da conta de numero {self.numero} é: {self.saldo}')

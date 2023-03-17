from mailbox import NotEmptyError


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def exibir(self):
        print(f' O nome do cliente: {self.nome} \n sobrenome {self.sobrenome} \n e cpf {self.cpf}')
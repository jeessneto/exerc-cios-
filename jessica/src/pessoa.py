class Pessoa:
    def __init__(self, nome, cpf, endereco) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def __str__(self) -> str:
        return f"Nome: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"
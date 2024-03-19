from src.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, materia) -> None:
        super().__init__(nome, cpf, endereco)
        self.materia = materia

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Matrícula: {self.materia}"
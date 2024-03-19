from src.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, matricula) -> None:
        super().__init__(nome, cpf, endereco)
        self.__matricula = matricula

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Matricula: {self.__matricula}"


from src.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, materia) -> None:
        super().__init__(nome, cpf, endereco)
        self.materia = materia

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Materia: {self.materia}"

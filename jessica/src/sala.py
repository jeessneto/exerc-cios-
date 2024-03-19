# sala.py
from src.aluno import Aluno
from src.professor import Professor

class Sala:
    def __init__(self, numero_sala) -> None:
        self.numero = numero_sala
        self.aluno = []
        self.professor = []

    def set_aluno(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            self.aluno.append(aluno)
        else:
            raise Exception("Precisa ter um aluno valido")

    def set_professor(self, professor: Professor):
        if isinstance(professor, Professor):
            self.professor.append(professor)
        else:
            raise Exception("Precisa ter um professor validdo")

    def __str__(self) -> str:
        alunos_str = "\n".join(str(aluno) for aluno in self.aluno)
        professores_str = "\n\n".join(str(professor) for professor in self.professor)
        return f"Turma: {self.numero}\nAlunos:\n{alunos_str}\n\nProfessores:\n{professores_str}"

from src.aluno import Aluno
from src.pessoa import Pessoa
from src.sala import Sala
from src.professor import Professor

if __name__ == "__main__":
    aluno1 = Aluno("Miguel","12345678908","Isabel Cristina Campos, 58, Santa Efigenia", "12354576")
    professor1 = Professor("Mariana", "12334546776", " Quinze de Novembro, 234, Santa Efigenia", "Matematica")
    sala = Sala(45)
    sala.set_aluno(aluno1)
    sala.set_professor(professor1)
    print(sala)
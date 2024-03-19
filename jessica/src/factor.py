from  faker import Faker
import random
def factory():
    fake = Faker (['pt-br'])

    CURSO = [
            "engenharia de software"
            "cientista de dados"
            "programador web"
            "programador HTML SQN"
            
            ]
    TURMA = [
            "0012-2024"
            "0013-2024"
            "0014-2024"
            "0015-2024"
        ]
    lista_pessoas = []
    nome = fake.name()
    for i in range(50):
        
        pessoas = {
            "nome": nome,
            "endereço": fake.address(),
            "email": f"{nome}@{fake.email().split('@')[1]}".replace(' ','_').lower(),
            "cpf": fake.cpf(),
            "curso": random.choice(CURSO),
            "turma": random.choice(TURMA),
            }
        lista_pessoas.append(pessoas)
    return lista_pessoas 

print(factory())
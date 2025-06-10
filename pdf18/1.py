# 01) A partir da listagem dos alunos matriculados em duas disciplinas, determine quais são os alunos matriculados nas duas disciplinas ao mesmo tempo.

disciplina1 = ["Ana", "Bruno", "Carla", "Diego"]
disciplina2 = ["Bruno", "Carla", "Eduardo", "Fernanda"]

alunos_ambas = []

for aluno in disciplina1:
    if aluno in disciplina2:
        alunos_ambas.append(aluno)

print("Alunos matriculados nas duas disciplinas:")
for aluno in alunos_ambas:
    print(aluno)

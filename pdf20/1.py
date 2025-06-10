# 01) Faça um programa que leia várias notas de vários alunos e armazene em um dicionário (o nome é a chave e as notas os valores). Faça um programa que mostre o nome do aluno e a média do aluno.

notas_alunos = {}

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para terminar): ")
    if nome.lower() == "sair":
        break
    
    notas_str = input(f"Digite as notas de {nome} separadas por espaço: ")
    lista_notas = [float(n) for n in notas_str.split()]
    
    notas_alunos[nome] = lista_notas

print("\nMédia dos alunos:")
for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas) if notas else 0
    print(f"{aluno}: {media:.2f}")
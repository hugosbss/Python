# 01) Existem dois arquivos. O primeiro, alunos.txt, contem o nome de N alunos. E o segundo, notas.txt, contem as notas dos N alunos (cada linha do arquivo contem uma ou mais notas do mesmo aluno separadas por vírgula). Crie um terceiro arquivo, onde cada linha contenha o nome do aluno mais sua respectiva média.

arquivo_alunos = open("Documentos/ADS/talon/pdf16/alunos.txt", "r")
lista_alunos = arquivo_alunos.readlines()
arquivo_alunos.close()

arquivo_notas = open("Documentos/ADS/talon/pdf16/notas.txt", "r")
lista_notas = arquivo_notas.readlines()
arquivo_notas.close()

arquivo_media = open("Documentos/ADS/talon/pdf16/media.txt", "w")
for i in range(len(lista_alunos)):
    nome = lista_alunos[i].strip()
    linha_notas = lista_notas[i].strip()
    notas = linha_notas.split(",")

    soma = 0
    for nota in notas:
        soma += float(nota)

    media = soma / len(notas) if notas else 0

    arquivo_media.write(f"{nome} {media:.2f}\n")

arquivo_media.close()

print("Arquivo media.txt criado com sucesso!")
# 03) Faça um programa que retorne uma frase sem os espaços em branco.

def remover_espacos(frase):
    return frase.replace(" ", "")

frase = input("Digite uma frase: ")
print("Frase sem espaços:", remover_espacos(frase))
# 01) Faça um programa que receba um vetor com 20 posições e rotacione esse vetor para a direita (novo vetor) e para a esquerda (novo vetor)

vetor = [int(input(f"Digite o valor da posição {i + 1}: ")) for i in range(20)]

# Rotação para a direita
vetor_direita = [vetor[-1]] + vetor[:-1]

# Rotação para a esquerda
vetor_esquerda = vetor[1:] + [vetor[0]]

print("Vetor original:", vetor)
print("Vetor rotacionado para a direita:", vetor_direita)
print("Vetor rotacionado para a esquerda:", vetor_esquerda)
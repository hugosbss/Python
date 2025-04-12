# 02) Faça um programa que sorteie 10 número aleatório e mostre a quantidade de números maiores que a média e menores que a média.

import random

vetor = []
for i in range(10):
    valor= int(input(f"Digite o valor da posição {i + 1}: "))
    vetor.append(valor)

# SORTEIA UM NÚMERO ALEATÓRIO
i = random.randint(0, len(vetor) - 1)
print(f"Numero sorteado: {vetor[i]}")

# CALCULA A MÉDIA
media = sum(vetor) / len(vetor)

maiores = 0
menores = 0
for numero in vetor:
    if numero > media:
        maiores += 1
    elif numero < media:
        menores += 1
print("Quantidade de números maiores que a média:", maiores)
print("Quantidade de números menores que a média:", menores)
# 03) Faça um programa que inverta uma lista com 5 posições em utilizar variáveis auxiliares (utilize apenas a própria lista).

lista = [int(input(f"Digite o valor da posição {i + 1}: ")) for i in range(5)]

for i in range(len(lista) // 2):
    # Lógica para inverter a lista
    lista[i], lista[-i - 1] = lista[-i - 1], lista[i]

print("Lista invertida:", lista)
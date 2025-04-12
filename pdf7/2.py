# 02) Faça um programa que leia n valores fornecidos pelo usuário e calcule a soma de seus quadrados.

N = int(input("Digite a quantidade de números: "))
Soma = 0
for i in range (N):
    num = int(input("Digite um número: "))
    Soma += num ** 2
print("A soma dos quadrados é:", Soma)
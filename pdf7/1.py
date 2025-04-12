# 01) Faça um programa para verificar se um número é triangular. Um número é triangular se for o produto de três números inteiros consecutivos.

X = int(input("Digite um número:"))

a = 1
b = 2
c = 3

while a * b * c <= X:
    if a * b * c == X:
        print("O numero é triangular")
        break
    a += 1
    b += 1
    c += 1
else:
    print("O numero não é triangular")
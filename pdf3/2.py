# 02) Faça um programa que leia 3 valores e mostre a soma de seus inversos.
valores = float (input('Digite 3 valores:'))
valores2 = float (input('Digite 3 valores:'))
valores3 = float (input('Digite 3 valores:'))
soma = (1/valores) + (2/valores2) + (3/valores3)
print(f'A soma dos inversos é: {soma:.2f}')
# 02) Faça um programa que leia os 3 lados de um triângulo e verifique se os 3 lados formam ou não um triângulo.

X = float(input('Digite o primeiro lado do triangulo: '))
Y = float(input('Digite o segundo lado do triangulo: '))
Z = float(input('Digite o terceiro lado do triangulo: '))
# Verifica se os lados formam um triângulo
if (X + Y > Z) and (X + Z > Y) and ( Y + Z > X):
    print('Os lados formam um triangulo')
else:
    print('Os lados não formam um triangulo')
# 01) Faça um programa que calcule o IMC de uma pessoa e informe a classificação segundo os intervalos: Abaixo do Peso = abaixo de 18,5 Peso Normal = entre 18,5 e 25 Acima do Peso = entre 25 e 30 Obeso = acima de 30

IMC = float(input('Informe o seu IMC: '))
if IMC < 18.5:
    print('Abaixo do Peso')
    if IMC >= 18.5:
        print('Peso Normal')
    if IMC < 25:
        print('Peso Normal')
    if IMC >= 25:
        print('Acima do Peso')
    if IMC < 30:
        print('Acima do Peso')
    if IMC >= 30:
        print('Obeso')
else:
    print('Obeso')
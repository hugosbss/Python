# 04) Faça um programa que receba a data de nascimento de uma pessoa e fale qual o signo dessa pessoa.

Nascimento = float(input('Digite o dia do seu nascimento: '))
Mes = float(input('Digite o mês do seu nascimneto: '))
Ano = float(input('Digite o ano do seu nascimento: '))

if (Mes == 1 and Nascimento >= 20) or (Mes == 2 and Nascimento <= 18):
    print('Seu signo é Aquário')
if (Mes == 2 and Nascimento >= 19) or (Mes == 3 and Nascimento <= 20):
    print('Seu signo é Peixes')
if (Mes == 3 and Nascimento >= 21) or (Mes == 4 and Nascimento <= 19):
    print('Seu signo é Áries')
if (Mes == 4 and Nascimento >= 20) or (Mes == 5 and Nascimento <= 20):
    print('Seu signo é Touro')
if (Mes == 5 and Nascimento >= 21) or (Mes == 6 and Nascimento <= 20):
    print('Seu signo é Gêmeos')
if (Mes == 6 and Nascimento >= 21) or (Mes == 7 and Nascimento <= 22):
    print('Seu signo é Câncer')
if (Mes == 7 and Nascimento >= 23) or (Mes == 8 and Nascimento <= 22):
    print('Seu signo é Leão')
if (Mes == 8 and Nascimento >= 23) or (Mes == 9 and Nascimento <= 22):
    print('Seu signo é Virgem')
if (Mes == 9 and Nascimento >= 23) or (Mes == 10 and Nascimento <= 22):
    print('Seu signo é Libra')
if (Mes == 10 and Nascimento >= 23) or (Mes == 11 and Nascimento <= 21):
    print('Seu signo é Escorpião')
if (Mes == 11 and Nascimento >= 22) or (Mes == 12 and Nascimento <= 21):
    print('Seu signo é Sagitário')
if (Mes == 12 and Nascimento >= 22) or (Mes == 1 and Nascimento <= 19):
    print('Seu signo é Capricórnio')
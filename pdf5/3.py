# 03) Faça um programa que receba as coordenadas de um ponto e retorne em qual quadrante esse ponto está localizado.

coordenadas = float(input ('Digite as coordenadas do ponto (x, y): '))
# Receber as coordenadas separadamente
x = float(input('Digite a coordenada X: '))
y = float(input('Digite a coordenada Y: '))

# Verificar em qual quadrante o ponto está localizado
if x > 0 and y > 0:
    print('O ponto está no Primeiro Quadrante.')
elif x < 0 and y > 0:
    print('O ponto está no Segundo Quadrante.')
elif x < 0 and y < 0:
    print('O ponto está no Terceiro Quadrante.')
elif x > 0 and y < 0:
    print('O ponto está no Quarto Quadrante.')
elif x == 0 and y != 0:
    print('O ponto está sobre o eixo Y.')
elif y == 0 and x != 0:
    print('O ponto está sobre o eixo X.')
else:
    print('O ponto está na origem (0, 0).')

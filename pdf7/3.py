# 03) Calcule o quociente e o resto da divisão de A por B utilizando apenas soma e subtração.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
quociente = 0
resto = A
while resto >= B:
    resto -= B
    quociente += 1
print("O quociente é:", quociente)
print("O resto é:", resto)
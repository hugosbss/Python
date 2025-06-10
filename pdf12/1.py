# 01) Faça uma rotina para calcular as raízes de uma equação do 2º grau. A rotina receberá os valores de a, b e c. E deverá retornar o tipo das raízes e os valores das raízes.

def calcular_raizes(a, b, c):
    if a == 0:
        return "Não é equação do 2º grau"
    
    delta = b**2 - 4*a*c
    
    if delta >= 0:
        r1 = (-b + delta**0.5) / (2*a)
        r2 = (-b - delta**0.5) / (2*a)
        if delta == 0:
            return "Raiz real dupla", r1
        else:
            return "Duas raízes reais", r1, r2
    else:
        real = -b / (2*a)
        imag = ((-delta)**0.5) / (2*a)
        raiz1 = f"{real} + {imag}i"
        raiz2 = f"{real} - {imag}i"
        return "Duas raízes complexas", raiz1, raiz2

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(calcular_raizes(a, b, c))
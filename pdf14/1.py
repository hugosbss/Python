# 01) Faça um programa que retorne a quantidade de vogais de uma frase 

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

frase = input("Digite uma frase: ")
print("Quantidade de vogais:", contar_vogais(frase))
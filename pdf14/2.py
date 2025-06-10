# 02) Faça um programa que leia uma frase e retorne a frase sem as vogais. 

def remover_vogais(frase):
    vogais = "aeiouAEIOU"
    resultado = ""
    for letra in frase:
        if letra not in vogais:
            resultado += letra
    return resultado

frase = input("Digite uma frase: ")
print("Frase sem vogais:", remover_vogais(frase))
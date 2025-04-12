# 04) Faça um programa que calcule a quantidade de dias corridos entre duas datas.

data1 = input("Digite a primeira data (dd/mm/aaaa): ").split("/")
data2 = input("Digite a segunda data (dd/mm/aaaa): ").split("/")

dia1, mes1, ano1 = map(int, data1)
dia2, mes2, ano2 = map(int, data2)

# Convertendo tudo para dias corridos
dias1 = ano1 * 365 + mes1 * 30 + dia1
dias2 = ano2 * 365 + mes2 * 30 + dia2

diferenca = abs(dias2 - dias1)
print("A quantidade de dias corridos é:", diferenca)
# 03) Faça um programa que leia o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento. Mostre o nome do produto e o valor total da venda.
Produto = input('Digite o nome do produto: ')
Quantidade = float (input('Digite a quantidade comprada:'))
ValorUnitario = float(input('Digite o valor unitario: '))
Desconto = float (input('Digite o percentual de desconto:'))
ValorTotal = (Quantidade * ValorUnitario) - (Quantidade * ValorUnitario * Desconto / 100)

print (f'Produto: {Produto}')
print (f'Valor Total: R${ValorTotal:.2f}')

# ':.2f' formata o valor para duas casas decimais
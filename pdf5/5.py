# 05) Faça um programa que receba o salário de um vendedor e total de vendas de um mês. Acrescentar ao salário um prêmio de acordo com os intervalos a seguir. Mostrar o salário do vendedor com a premiação.
# Vendas de 1.000,00 a 5.000,00 = Premiação de 500,00
# Vendas de 5.000,01 a 7.500,00 = Premiação de 750,00
# Vendas maiores que 7.500,00 = Premiação de 1.000,00

salario = float(input('Digite o salário do vendedor: '))
vendas = float(input('Digite as vendas do mês: '))

premio = 0  # Inicializando o prêmio como 0
if vendas >= 1000 and vendas <= 5000:
    premio = 500
elif vendas > 5000 and vendas <= 7500:  # Usei "elif" para simplificar
    premio = 750
elif vendas > 7500:
    premio = 1000
elif vendas <= 1000:
    print('Vendas abaixo de 1000,00 não têm premiação.')

salario += premio  # Soma do salário e prêmio
print(f'O salário do vendedor é: R${salario:.2f}')
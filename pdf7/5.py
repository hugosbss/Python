# 05) Faça um programa que contenha um menu para as 4 operações básicas (Soma, Subtração, Produto e Divisão) mais a opção Sair. O programa deve simular uma calculadora e resolver a operação entre os 2 operandos.

print("Selecione as opções abaixo:")
soma = 1
subtracao = 2
multiplicacao = 3
divisao = 4
sair = 5
while True:
    print("Escolha uma opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    opcao = int(input("Digite a opção desejada: "))

    if opcao == sair:
            print("Voce saiu")
            break # SAIR

    if opcao in [1, 2, 3, 4]:
        num = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == soma:
            resultado = num + num2
            print(f"Resultado: {resultado}")

        elif opcao == subtracao:
            resultado = num - num2
            print(f"Resultado: {resultado}")

        elif opcao == multiplicacao:
            resultado = num * num2
            print(f"Resultado: {resultado}")

        elif opcao == divisao:
            if num2 == 0:
                print("Não é possível dividir por zero")
            else:
                resultado = num / num2
                print(f"Resultado: {resultado}")
        else:
            print("Digite uma opção válida")
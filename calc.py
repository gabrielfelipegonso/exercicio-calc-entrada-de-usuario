def calculadora():
    while True:
        print("Selecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = input("Digite o número para a operação correspondente: ")

        if operacao == '0':
            print("Encerrando a calculadora.")
            break
        elif operacao not in {'1', '2', '3', '4'}:
            print("Essa opção não existe.")
            continue

        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if operacao == '1':
            resultado = num1 + num2
            print("Resultado:", resultado)
        elif operacao == '2':
            resultado = num1 - num2
            print("Resultado:", resultado)
        elif operacao == '3':
            resultado = num1 * num2
            print("Resultado:", resultado)
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado:", resultado)
            else:
                print("Erro: Divisão por zero!")

        print()  # Linha em branco para separar as operações

# Chamar a função para iniciar a calculadora
calculadora()
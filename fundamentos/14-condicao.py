# Receber os números e a operação do usuário
num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
operation = input("Digite a operação a ser realizada: soma (+), subtração (-), multiplicação (*) ou divisão (/):\n")

# Verificar qual operação realizar
if operation == "+":
    # Calcular a soma
    result = num1 + num2
elif operation == "-":
    # Calcular a subtração
    result = num1 - num2
elif operation == "*":
    # Calcular a multiplicação
    result = num1 * num2
elif operation == "/":
    # Verificar se o divisor não é zero para evitar erro
    if num2 != 0:
        # Calcular a divisão
        result = num1 / num2
    else:
        # Divisor é zero: informar erro e definir resultado padrão
        print("Erro: Divisão por zero não é permitida.")
        result = None
else:
    # Operação inválida: informar erro e definir resultado padrão
    print("Operação inválida.")
    result = None

# Exibir o resultado, caso tenha sido calculado corretamente
if result is not None:
    print(f"O resultado é: {result}")

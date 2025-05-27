# Input
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2 # Sobra de divisão
exp = num1 ** num2 # Exponenciação

# Imprime aritméticos
print(f"\nA potência do número {num1} por {num2} é: {exp}")
print(f"O resto da divisão de {num1} por {num2} é: {mod}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

# Imprime comparações
print("\nO número",num1, "é maior que",num2, "?",bigger)
print(f"O número {num1} é menor ou igual a {num2}? {smaller_equal}")

# Atribuição
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1
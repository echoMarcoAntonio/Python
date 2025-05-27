movieName = "Top Gun"

"""
string[início:fim]

O índice começa na posição 0 e vai até o índice final - 1.

"""

# 1 - Buscar toda string a partir da primeira posição:
print(movieName[0:])

# 2 - Buscar toda string até a última posição:
print(movieName[:7])

# 3 - Buscar toda string da terceira até a última posição:
print(movieName[2:])

"""
string[início:fim:passo]

Mantém-se o mesmo comportamento [início:fim]
[passo] determina o incremento. Por padrão o número 1.

"""

# 4 - Buscar toda string de 2 em 2 caracteres por meio do incremento/passo:
print(movieName[::2])

# 5 - Buscar toda string de 2 em 2 caracteres nos índices ímpares:
print(movieName[1::2])

# 6 - Inverter uma string de trás para frente:
print(movieName[::-1]) # incremento negativo
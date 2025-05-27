# Dados de string:
movieName = "Top Gun Maverick"
movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura,
sendo muito consagrado na indústria dos filmes.
"""

# Transforma todos os caracteres da string em maiúsculo.
print(movieName.upper())  
# Saída: TOP GUN MAVERICK

# Transforma todos os caracteres da string em minúsculo.
print(movieName.lower())  
# Saída: top gun maverick

# Transforma apenas o primeiro caractere em maiúsculo e o restante em minúsculo.
print(movieName.capitalize())  
# Saída: Top gun maverick

# Transforma o primeiro caractere de cada palavra em maiúsculo.
print(movieName.title())  
# Saída: Top Gun Maverick

# Centraliza a string em 30 caracteres, preenchendo com o caractere '-' nas laterais.
# Se o número passado for menor que o comprimento da string, o método não altera nada.
print(movieName.center(30, '-'))  
# Saída: ------Top Gun Maverick-------

# Retorna o índice da primeira ocorrência da letra "u" (case-sensitive).
print(movieName.find("u"))  
# Saída: 5 (posição da primeira letra "u")

# Retorna o índice da primeira ocorrência da letra "o".
print(movieName.find("o"))  
# Saída: 1

# Substitui a palavra "Top" por "Matrix" na string.
print(movieName.replace("Top", "Matrix"))  
# Saída: Matrix Gun Maverick

# Divide a string movieDescription em partes separadas por vírgula.
print(movieDescription.split(','))  
# Saída: 
# ['\n    Top Gun Maverick é um filme de aviação e aventura',
#  '\nsendo muito consagrado na indústria dos filmes.\n']

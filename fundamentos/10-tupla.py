# Definição de uma tupla contendo 5 títulos de filmes
filmsTuple = (
    "Interstellar",
    "Inception",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction"
)

# print(type(filmsTuple))

# Métodos reaproveitados de "8-lista.py"

# 1 - Exibe a tupla completa com os 5 filmes
print(filmsTuple)

# 2 - Exibe os 2 primeiros filmes da tupla
print(filmsTuple[:2])

# 3 - Exibe os 3 primeiros filmes da tupla
print(filmsTuple[:3])

# 4 - Exibe o último filme da tupla
print(filmsTuple[-1])

# 5 - Exibe os filmes a partir de uma determinada posição
print(filmsTuple[1:4])  # Do segundo ao quarto filme (índices 1 a 3)
print(filmsTuple[3:])   # Do quarto filme até o final (índice 3 em diante)

# Único método reaproveitável de "9-metodo_lista"

# 6 - Localiza o nome do filme e imprime seu índice
print(filmsTuple.index("The Dark Knight"))

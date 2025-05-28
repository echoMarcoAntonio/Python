# Lista com informações sobre o filme Matrix
filmMatrix = ["Matrix", 1999, 8.7, True]
print(filmMatrix)

# Lista com 5 filmes, cada um representado por outra lista com:
# título, ano de lançamento, nota do IMDb e se já foi assistido (True ou False)
filmList = [
    ["Interstellar", 2014, 8.6, True],
    ["Inception", 2010, 8.8, True],
    ["The Godfather", 1972, 9.2, False],
    ["The Dark Knight", 2008, 9.0, True],
    ["Pulp Fiction", 1994, 8.9, False]
]

# 1 - Exibe a lista completa dos 5 filmes
print(filmList)

# 2 - Exibe os 2 primeiros filmes da lista
print(filmList[:2])

# 3 - Exibe os 3 primeiros filmes da lista
print(filmList[:3])

# 4 - Exibe o último filme da lista
print(filmList[-1])

# 5 - Exibe filmes de uma posição em diante
print(filmList[1:4])

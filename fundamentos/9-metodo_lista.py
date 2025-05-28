# Lista contendo apenas nomes de filmes
filmList = [
    "Interstellar",
    "Inception",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction"
]

# 1 - Verifica e imprime a quantidade total de filmes na lista
print(len(filmList))

# 2 - Encontra e imprime o índice do filme "The Dark Knight"
print(filmList.index("The Dark Knight"))

# 3 - Adiciona um novo filme ao final da lista
filmList.append("The Lord of The Rings")
print(filmList)

# 4 - Ordena os filmes em ordem alfabética
filmList.sort()
print(filmList)

# 5 - Cria uma cópia da lista e remove "Pulp Fiction" da cópia
filmsCopy = filmList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 6 - Limpa todos os itens da lista original (filmList fica vazia)
filmList.clear()
print(filmList)

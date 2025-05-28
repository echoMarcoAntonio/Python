# Dicionário com informações variadas
filmInception = {
    # Propriedade | Valor
    "title": "Inception",
    "releaseYear": 2010,
    "imdbRating": 8.8,
    "genre": ["Sci-fi", "Action", "Thriller"]
}

"""
print(filmInception)
print(len(filmInception))
print(type(filmInception))
"""

# 1 - Recuperar elementos pelo nome da chave
# Acesso direto: retorna o valor associado à chave "genre" (uma lista de gêneros)
print(filmInception["genre"])
# Método get(): retorna o valor da chave "imdbRating" ou None se a chave não existir
print(filmInception.get("imdbRating"))

# 2 - Apenas as chaves do dicionário (exemplo: 'title', 'releaseYear', etc.)
print(filmInception.keys())

# 3 - Apenas os valores do dicionário (exemplo: 'Inception', 2010, 8.8, lista de gêneros)
print(filmInception.values())

# 4 - Pares chave-valor do dicionário como tuplas (exemplo: ('title', 'Inception'))
print(filmInception.items())

# 5 - Adicionar itens ao dicionário (chave-valor)
filmInception["director"] = "Cristopher Nolan"
print(filmInception)

# 6 - Atualização de items já adicionados
filmInception.update({"imdbRating": 8.7})
print(filmInception)

# 7 - Remover item do direório
filmInception.pop("director")
print(filmInception)

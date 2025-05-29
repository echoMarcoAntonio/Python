import pprint  # Importar o módulo 'pprint' para exibir dicionários grandes de forma organizada

# Criar um dicionário principal com informações de filmes.
# Cada chave (nome do filme em minúsculas) mapeia para um outro dicionário com detalhes do filme.
moviesDict = {
    "inception": {
        "title": "Inception",
        "releaseYear": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar": {
        "title": "Interstellar",
        "releaseYear": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "the dark knight": {
        "title": "The Dark Knight",
        "releaseYear": 2008,
        "imdbRating": 9.0,
        "genre": ["Sci-fi", "Action", "Thriller"]
    }
}

# Criar um objeto 'PrettyPrinter' para exibir dicionários formatados com indentação
pp = pprint.PrettyPrinter(depth=4)

# Exibir todo o dicionário 'moviesDict' com indentação para facilitar a leitura
pp.pprint(moviesDict)

# 1 - Acessar um valor dentro de um dicionário aninhado:
#     Acessar o valor associado à chave "genre" dentro do filme "interstellar".
#     Retorna a lista de gêneros do filme.
print(moviesDict["interstellar"]["genre"])

# 2 - Adicionar uma nova propriedade ao dicionário interno do filme "inception":
#     Adicionar a chave "director" com o valor "Christopher Nolan".
#     Demonstra como expandir um dicionário aninhado dinamicamente.
moviesDict["inception"]["director"] = "Christopher Nolan"

# Exibir os dados do filme "inception" após a adição da nova propriedade
print(moviesDict["inception"])

# Exibir os dados do filme "the dark knight" como referência de comparação
print(moviesDict["the dark knight"])

# 3 - Remover um item (filme) inteiro do dicionário principal:
#     Usar a instrução 'del' para excluir o par chave-valor correspondente ao filme "interstellar".
#     Remove completamente o registro desse filme do dicionário.
del moviesDict["interstellar"]

# Exibir o dicionário após a remoção para confirmar que "interstellar" foi excluído
pp.pprint(moviesDict)

# Definição de um set contendo 5 títulos de filmes
filmsSet = {    
    "Interstellar",
    "Inception",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction"
}

# 1 - Exibe a quantidade de elementos no set
print(len(filmsSet))

# True e 1 são tratados como o mesmo valor em sets
exampleSet = {"Inception", True, 1, 8.7}
print(exampleSet)  # 'True' e '1' ocupam a mesma posição; apenas um será mantido

# 3 - Adiciona novos itens ao set (valores duplicados são ignorados automaticamente)
filmsSet.update({"Whiplash", 8.7})  # 'Inception' já existe e não será duplicado

# 4 - Remove itens do set
filmsSet.remove(True)   # Remove True, se estiver presente
filmsSet.remove(8.7)    # Remove 8.7, se estiver presente
print(filmsSet)

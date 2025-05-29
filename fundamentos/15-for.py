# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

print("\n.1")

# 1 - Iterar sobre todos os elementos da lista
# Usar laço for para exibir cada item da lista
for movie in moviesList:
    print(movie)

print("\n.2")

# 2 - Encerrar o loop ao atingir uma condição
# Usar break para sair do loop imediatamente quando a condição for satisfeita
for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)

print("\n.3")

# 3 - Ignorar uma iteração e seguir para a próxima
# Usar continue para pular o restante da iteração atual quando a condição for satisfeita
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)

print("\n.4")

# 4 - Calcular média de avaliações de um filme
# Solicitar nome do filme e número de avaliações
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

# Inicializar acumulador de notas
total = 0

# Repetir coleta de notas conforme a quantidade informada
for i in range(movieRating):
    rank = float(input("Digite a nota para o filme:\n"))
    total += rank

# Evitar divisão por zero ao calcular a média
if movieRating > 0:
    average = total / movieRating
else:
    average = 0

# Exibir resultado final
print(f"Média de avaliação do filme {movieName} é: {average:.2f}")

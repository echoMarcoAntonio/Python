# Definir lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterar pelos valores da lista usando estrutura while
index = 0
while index < len(moviesList):
    # Imprimir o valor atual da lista na posição 'index'
    print(moviesList[index])
    # Incrementar o índice para acessar o próximo item
    index += 1

# 2 - Interromper o loop quando um valor específico for encontrado
index = 0
while index < len(moviesList):

    # 'index' representa a posição atual (inteiro) na lista
    # moviesList[index] acessa o valor armazenado nessa posição
    if moviesList[index] == "Inception":
        # Interromper o loop ao encontrar o valor "Inception"
        break

    # Imprimir o valor atual antes de incrementar o índice
    print(moviesList[index])
    # Incrementar o índice para acessar o próximo item
    index += 1

# 3 - Continuar o loop quando condição atendida (pular a iteração atual)
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        # Incrementar o índice para pular a iteração atual
        index += 1
        # Continuar para a próxima iteração do loop
        continue

    # Imprimir o valor atual antes de incrementar o índice
    print(moviesList[index])
    # Incrementar o índice para acessar o próximo item
    index += 1

# 4 - Coletar avaliações de um filme usando while

# Solicitar o nome do filme ao usuário
movieName = input("Digite o nome do filme:\n")
# Solicitar a quantidade de avaliações e converter para inteiro
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

# Inicializar acumulador para a soma e contador
total = 0
count = 0

# Repetir enquanto o número de avaliações realizadas for menor que o desejado
while count < movieRating:
    # Solicitar a nota da avaliação e converter para float
    note = float(input("Digite a nota para o filme:\n"))
    # Somar a nota ao total acumulado
    total += note
    # Incrementar o contador de avaliações realizadas
    count += 1

# Verificar se houve avaliações para evitar divisão por zero
if movieRating > 0:
    # Calcular a média das avaliações
    average = total / movieRating
else:
    # Definir média como zero caso não haja avaliações
    average = 0

# Exibir a média formatada
print(f"Média de avaliação do filme {movieName} é: {average:.2f}")

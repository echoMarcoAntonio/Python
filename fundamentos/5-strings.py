# Demonstração da característica Case Sensitive do Python
movieName = "Top Gun Maverick"
movieName2 = "top Gun"
print(movieName == movieName2) # False

# Exemplo de String multi-linha (imprime diretamente conforme a identação)
movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura,
sendo muito consagrado na indústria dos filmes.
"""

print("\n",movieName)

# Multiplicação de Strings
line = "="
print(line*55)

print(movieDescription)

# Busca de uma palavra dentro de um texto
print("Top" in movieName)
print("ação"in movieName)
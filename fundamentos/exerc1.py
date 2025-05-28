"""
1 - Escreva um programa que lê dois nomes e retorne uma string
    formatada no formato "ÚltimoNome, PrimeiroNome".

2 - Inverta a ordem das palavras em uma string fornecida.

3 - Verifique se uma string fornecida é um palíndromo 
    (pode ser lida de trás pra frente.)
"""

# -------------------------------
# Ex1 - Formatar dois nomes
# -------------------------------

# Recebe o primeiro nome via input do usuário
name1 = input("Digite o primeiro nome: ")

# Recebe o segundo nome (não necessariamente sobrenome)
name2 = input("Digite o segundo nome: ")

# Formata os nomes com letra inicial maiúscula
# e reorganiza no formato "SegundoNome, PrimeiroNome"
formattedName = f"\n{name2.title()}, {name1.title()}\n"

# Exibe a string formatada
print(formattedName)


# -------------------------------
# Ex2 - Inverter palavras do texto
# -------------------------------

# Texto base:
text = """
Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold
"""

# Divide o texto em uma lista de palavras, usando espaço como separador padrão
words = text.split()

# Inverte a lista de palavras e usa o método join(), 
# chamado pela string separadora (" "), para unir a lista em uma única string.
# join() recebe uma lista de strings e retorna uma string com os elementos separados pelo separador.
invertedText = " ".join(words[::-1])


# Exibe o texto com as palavras em ordem invertida
print(f"{invertedText}\n")


# -------------------------------
# Ex3 - Verificar palíndromos
# -------------------------------

# Lista de textos a serem verificados
texts = ["ovo", "bolo", "arara"]

# Loop para percorrer cada string da lista
for text in texts:
    # Formata o texto: remove espaços e transforma em minúsculo
    text_format = text.lower().replace(" ", "")
    
    # Compara o texto formatado com ele mesmo invertido
    palindromo = text_format == text_format[::-1]

    # Exibe o resultado da verificação (True || False)
    print(palindromo)

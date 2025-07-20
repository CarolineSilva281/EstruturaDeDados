# Exercício 5 – Conjuntos com vogais e letras de uma palavra, mostrar letras em comum
vogais = {"a", "e", "i", "o", "u"}
palavra = input("Digite uma palavra: ").lower()
letras_palavra = set(palavra)  # Cria conjunto com letras da palavra

# Interseção entre conjuntos (letras em comum)
comum = vogais.intersection(letras_palavra)
print("Letras em comum com as vogais:", comum)

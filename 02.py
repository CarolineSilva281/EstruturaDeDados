# Exercício 2 – Receber 3 números do usuário, guardar em lista e mostrar média

numeros = []

# Pedindo os 3 números ao usuário
for i in range(3):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Exibindo a lista completa
print("Números digitados:", numeros)

# Calculando a média dos números
media = sum(numeros) / len(numeros)

# Exibindo a média
print("Média dos números:", media)


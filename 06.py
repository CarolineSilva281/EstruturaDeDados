# Exercício 6 – Set com 5 números digitados (podem repetir), mostrar sem repetições e quantos únicos
numeros_digitados = []
# Coletando 5 números
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros_digitados.append(numero)

# Convertendo para set para eliminar repetições
conjunto = set(numeros_digitados)

print("Números digitados (sem repetições):", conjunto)
print("Quantidade de valores únicos:", len(conjunto))

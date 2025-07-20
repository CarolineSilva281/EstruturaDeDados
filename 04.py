# Exercício 4 – Tupla com 4 números do usuário, contar pares e verificar se há 10
numeros = []
# Pedindo os 4 números
for i in range(4):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

# Convertendo para tupla
tupla = tuple(numeros)

# Contando pares
pares = 0
for n in tupla:
    if n % 2 == 0:
        pares += 1

# Verificando se 10 está na tupla
tem_dez = 10 in tupla

print("Tupla:", tupla)
print("Quantidade de números pares:", pares)
print("O número 10 está na tupla?", tem_dez)

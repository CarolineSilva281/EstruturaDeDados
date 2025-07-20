# Exercício 8 – Dicionário com alunos e notas, mostrar todos e só os com nota >= 7
alunos = {
    "Alice": 9.0,
    "Bruno": 6.5,
    "Camila": 7.5,
    "Diego": 5.0,
    "Elisa": 8.2
}

# Mostrando dicionário completo
print("Notas dos alunos:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")

# Mostrando só os com nota >= 7
print("\nAlunos com nota maior ou igual a 7:")
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome}: {nota}")

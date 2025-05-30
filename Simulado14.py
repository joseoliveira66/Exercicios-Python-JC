def is_sorted_ascending(V):
    # Itera através do vetor e verifica se cada elemento é menor que o próximo
    for i in range(len(V) - 1):
        if V[i] > V[i + 1]:
            return False
    return True

# Solicita ao usuário que insira a quantidade de números no vetor
n = int(input("Digite a quantidade de números no vetor: "))

# Inicializa o vetor vazio
V = []

# Solicita ao usuário que insira os números um por um
for i in range(n):
    numero = int(input(f"Digite o número {i + 1}: "))
    V.append(numero)

# Chama a função para verificar se o vetor está em ordem crescente
ordenado = is_sorted_ascending(V)

# Exibe o resultado
print(f"O vetor está em ordem crescente? {ordenado}")

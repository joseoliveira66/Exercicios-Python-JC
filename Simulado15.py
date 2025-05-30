def zerar_matriz(n, m):
    # Cria uma matriz de tamanho n x m inicializada com zeros
    matriz = [[0 for _ in range(m)] for _ in range(n)]

    return matriz


# Solicita ao usuário que insira o número de linhas e colunas
n = int(input("Digite o número de linhas da matriz: "))
m = int(input("Digite o número de colunas da matriz: "))

# Chama a função para criar a matriz e zera todos os elementos
matriz_zerada = zerar_matriz(n, m)

# Exibe a matriz zerada
print("Matriz zerada:")
for linha in matriz_zerada:
    print(linha)

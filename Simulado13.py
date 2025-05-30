def contar_e_mostrar_impares(vetor):
    contagem_impares = 0
    numeros_impares = []

    for numero in vetor:
        if numero % 2 != 0:
            contagem_impares += 1
            numeros_impares.append(numero)

    return contagem_impares, numeros_impares


# Vetor fornecido no enunciado
vetor = [10, 7, 8, 7, 6, 5, 3, 3, 2, 1]

# Chama a função para contar e obter os números ímpares
quantidade_impares, numeros_impares = contar_e_mostrar_impares(vetor)

# Exibe a quantidade de elementos ímpares
print(f"A quantidade de elementos ímpares no vetor é: {quantidade_impares}")
# Exibe os números ímpares
print(f"Os números ímpares no vetor são: {numeros_impares}")



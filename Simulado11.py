def find_largest_number():
    largest = None
    while True:
        try:
            number = float(input("Digite um número (0 para parar): "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if number == 0:
            break

        if largest is None or number > largest:
            largest = number

    if largest is not None:
        print(f"O maior número digitado é: {largest}")
    else:
        print("Nenhum número foi digitado.")


# Chama a função para executar o algoritmo
find_largest_number()

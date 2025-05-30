def calcular_multa():
    peso_total = 0
    while True:
        try:
            peso = float(input("Digite o peso do peixe (ou 0 para parar): "))
        except ValueError:
            print("Por favor, insira um peso válido.")
            continue

        if peso == 0:
            break

        peso_total += peso

    excesso = max(0, peso_total - 50)
    multa = excesso * 4

    print(f"Peso total de peixes: {peso_total} kg")
    print(f"Excesso: {excesso} kg")
    print(f"Multa: R$ {multa:.2f}")


# Chama a função para executar o algoritmo
calcular_multa()

def calcular_peso(altura, sexo):
    if sexo.lower() == 'homem':
        return (72.7 * altura) - 58
    elif sexo.lower() == 'mulher':
        return (62.1 * altura) - 44.7
    else:
        return None

def main():
    while True:
        altura = float(input("Digite a altura (ou 0 para sair): "))
        if altura == 0:
            print('--------------FIM DO PROGRAMA------------------')
            break
        sexo = input("Digite o sexo (homem/mulher) : ").strip()
        if sexo == "":
            print('--------------FIM DO PROGRAMA------------------')
            break
        peso = calcular_peso(altura, sexo)
        if peso is not None:
            print(f"O peso sugerido é: {peso:.2f} kg")
        else:
            print("Sexo inválido. Tente novamente.")

if __name__ == "__main__":
    main()

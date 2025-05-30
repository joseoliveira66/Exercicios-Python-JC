numeros_maiores_que_100 = []  # Lista para armazenar números maiores que 100

while True:
    numero = int(input("Digite um número (0 para parar): "))  # Lê um número do usuário

    if numero == 0:  # Verifica se o número é zero
        break  # Sai do loop se o número for zero

    if numero > 100:  # Verifica se o número é maior que 100
        numeros_maiores_que_100.append(numero)  # Adiciona o número à lista

# Exibe os números maiores que 100
for numero in numeros_maiores_que_100:
    print(numero)

# Exibe a quantidade total de números maiores que 100
print("Quantidade total de números maiores que 100:", len(numeros_maiores_que_100))

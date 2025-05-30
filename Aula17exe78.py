# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista

'''numeros = list()

for n in range(0, 5):
    valor = int(input(f'Digite um numero para a posicao {n}: '))
    numeros.append(valor)

maior_valor = max(numeros)
menor_valor = min(numeros)

posicao_maior = numeros.index(maior_valor)
posicao_menor = numeros.index(menor_valor)

print(f'Os números digitados foram: {numeros}\n', end="")

print(f'O maior valor encontrado foi {maior_valor} na posicao {posicao_maior}, o menor valor encontrado foi {menor_valor} na posicao {posicao_menor} ')'''


# Cria uma lista vazia para armazenar os números digitados
listanum = []

# Inicializa as variáveis para o maior e menor valor
mai = 0
men = 0

# Lê 5 números do usuário e os adiciona à lista
for c in range(0, 5):
    # Lê um número e o converte para inteiro
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))

    # Verifica se é o primeiro número
    if c == 0:
        # Se for o primeiro, o maior e o menor são iguais ao primeiro número
        mai = men = listanum[c]
    else:
        # Compara o número atual com o maior e o menor
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

# Imprime um separador visual
print('=-' * 30)

# Imprime a lista de números digitados
print(f'Voce digitou os valores {listanum} ')

# Imprime o maior valor e suas posições
print(f'O maior valor digitado foi {mai}, nas posicoes, ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()

# Imprime o menor valor e suas posições
print(f'O menor valor digitado foi {men}, nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()

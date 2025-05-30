#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
#ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

# Inicializa uma lista vazia para armazenar os valores únicos
numeros = list()

while True:  # Inicia um loop infinito
    # Solicita um valor numérico ao usuário
    valor = int(input('Digite um valor: '))

    # Verifica se o valor não está na lista
    if valor not in numeros:
        # Adiciona o valor na lista
        numeros.append(valor)
        print('Valor adicionado com sucesso!!')
    else:
        # Informa que o valor já está na lista e não será adicionado
        print('Valor duplicado! Não vou adicionar..!')

    # Pergunta ao usuário se ele quer continuar
    parar = str(input('Quer continuar? [S/N] '))

    # Verifica se o usuário digitou 'N' ou 'n' para parar o loop
    if parar in 'Nn':
        break

# Imprime um separador decorativo
print('-=' * 30)

# Ordena a lista de valores únicos em ordem crescente
numeros.sort()

# Exibe os valores únicos digitados em ordem crescente
print(f'Os valores únicos digitados em ordem crescente são: {numeros}')


# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

while True:
    valores = input('Digite um numero ou [sair para parar]: ')
    if valores.lower() == 'sair':
        break

    numero = int(valores)
    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

numeros.sort()
pares.sort()
impares.sort()

print('-=' * 30)
print(f'Lista completa dos numeros digitados: {numeros}' )
print(f'Os números pares digitados foram: {pares}' )
print(f'Os números impares digitados foram: {impares}' )

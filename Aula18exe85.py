# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = [[], []]

for cont in range(0, 7):
    valor = int(input(f'Digite o {cont + 1}º numero: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print('-=' * 35)
print(f'Os numeros digitados foram {numeros} ')
print(f'Os números pares em ordem crescente digitados foram {numeros[0]} ')
print(f'Os números impares em ordem crescente digitados foram{numeros[1]} ')

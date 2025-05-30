# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa em Kg: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso registrado é: {} '.format(maior))
print('Os menor peso registrado é: {} '.format(menor))





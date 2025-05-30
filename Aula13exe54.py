# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date

data_atual = date.today().year

totmaior = 0
totmenor = 0
for i in range(7):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i + 1)))
    idade = data_atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('O total de pessoas maiores de idade foi de: {} '.format(totmaior))
print('O total de pessoas menores de idade foi de: {} '.format(totmenor))

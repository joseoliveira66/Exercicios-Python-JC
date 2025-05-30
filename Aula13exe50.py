# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar,
# desconsidere-o.

soma = 0
numeros_pares = []

for i in range(6):
    numero = int(input('Digite o {}º numero inteiro: '.format(i + 1)))
    if numero % 2 == 0:
        soma = soma + numero
        numeros_pares.append(numero)
if numeros_pares:
    print('Os numeros pares digitados foram {} '.format(numeros_pares))
    print('A soma dos numeros pares é {} '.format(soma))
else:
    print('Nenhum numero par foi digitado!!')

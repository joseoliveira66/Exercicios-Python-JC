# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

import random

numeros_aleatorios = tuple(random.randint(1, 100) for n in range(5))

print(f'Os valores sorteados foram: {numeros_aleatorios}')

print(f'O menor número da sequencia é: {min(numeros_aleatorios)}')
print(f'O maior numero da sequencia é: {max(numeros_aleatorios)}')

print('FIM DO PROGRAMA!!')

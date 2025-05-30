# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from html.parser import endtagfind

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

for num in range(n1, n2):
    if num % 2 == 0:
        print(num, end=' ')
print('\nNúmeros pares do intervalo de {} a {}'.format(n1, n2))

'''for num in range(n1, n2):
        print(num, end=' ')
print('\nNúmeros pares do intervalo de {} a {}'.format(n1, n2))'''


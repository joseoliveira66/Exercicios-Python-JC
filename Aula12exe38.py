# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número {} é maior que o segundo número {}'.format(n1, n2))
elif n1 < n2:
    print('O segundo número {} é maior que o primeiro número {}'.format(n2, n1))
else:
    print('Os dois números são iguais')


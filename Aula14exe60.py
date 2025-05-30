# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

'''from math import factorial

numero = int(input('Digite um número para calcularmos seu fatorial: '))
f = factorial(numero)
print('O fatorial de {} é {} '.format(numero, f))'''

'''resultado = 1
contador = 1

while contador <= numero:
    resultado *= contador
    contador += 1
print('O fatorial do número {} é {} '.format(numero, resultado))'''


n = int(input("Digite um número para calculo de fatorial: "))
c = n
f = 1
print('Calculando {}! = '.format(n), end="")
while c > 0:
    print(' {} '.format(c), end="")
    print(' x ' if c > 1 else ' = ', end="")
    f *= c
    c -= 1
print('{} '.format(f))

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print('O maior número entre ( {}, {} e {} ) é {} '.format(n1, n2, n3, maior))
print('O menor número entre ( {}, {} e {} ) é {} '.format(n1, n2, n3, menor))

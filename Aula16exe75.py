# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
from itertools import count

numeros = (int(input('Digite o primeiro número: ')),
int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')),
int(input('Digite o quarto número: '))
)

#numeros = (n1, n2, n3, n4)
print(f'Os números digitados foram: {numeros}')

qtde_noves = numeros.count(9)

if 3 in numeros:
    tres = numeros.index(3) + 1
    print(f'O primeiro número 3 apareceu na posição {tres} ')
else:
    print('O número três não foi digitado. ')

pares = [valor for valor in numeros if valor % 2 == 0]
print(f'Os valores pares digitados são: {pares}')
print(f'O número 9 apareceu {qtde_noves} vezes. ')

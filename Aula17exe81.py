# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados.
# B) A lista de valores ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.



numeros = []

while True:
    entrada = input('Digite um numero ou [sair para parar]: ')
    if entrada.lower() == 'sair':
        break
    numero = int(entrada)
    numeros.append(numero)

print('-=' * 30)
quantidade = len(numeros)
print(f'A quantidade de números digitada foi {quantidade}')

numeros.sort(reverse=True)
print(f'Os numeros em ordem decrecente são {numeros}')

if 5 in numeros:
    print('O número cinco está presente!!')
else:
    print('O número cinco não foi digitado!!')

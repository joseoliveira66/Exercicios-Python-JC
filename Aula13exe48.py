# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

'''s = 0

for num in range(1, 501):
    if num % 2 == 1:
        if num % 3 == 0:
            s = s + num
print('A soma dos valores multiplos de 3 do intervalo de 1 a 500 é {} '.format(s))'''

s = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        s = s + num
print('A soma dos valores multiplos de 3 do intervalo de 1 a 500 é {} '.format(s))
print('A quantidade de números contados e somados foi de: {} números. '.format(cont))

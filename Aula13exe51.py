# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = int(input('Digite quantos termos da PA: '))

print('Os primeiros {} da PA são: '.format(n))
for i in range(n):
    termo = a1 + i * r
    print(termo, end=" ")
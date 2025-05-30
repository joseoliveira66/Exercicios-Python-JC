# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = int(input('Digite quantos termos da PA: '))

print('Os primeiros {} da PA são: '.format(n))
for i in range(n):
    termo = a1 + i * r
    print(termo, end=" ")'''


primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end="")
    termo += razao
    cont += 1
print('FIM!!')

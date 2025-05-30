# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

'''def forma_triangulo (r1, r2, r3):
    if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
        return True
    else:
        return False'''

r1 = float(input('Digite o tamenho da primeira reta: '))
r2 = float(input('Digite o tamenho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os três lados formam um triângulo')
else:
    print('Os três lados não formam um triângulo')

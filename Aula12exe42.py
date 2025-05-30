# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#  – EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente, ESCALENO: todos os lados diferentes

r1 = float(input('Digite o valor do primeiro lado: '))
r2 = float(input('Digite o valor do segundo lado: '))
r3 = float(input('Digite o valor do terceiro lado '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um TRIÂNGULO. ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima não podem formar um triângulo. ')



# Ler um número e mostrar o dobro, o triplo e a raiz quadrada
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
#print('Analisando o número {}, seu dobro é {}, seu triplo é {}, sua raiz quadrada é {}'.format(n, d, t, r))
print('Analisando o número {}, seu dobro é {}, seu triplo é {}, sua raiz quadrada é {}'.format(n, (n*2), (n*3), (n**2)))
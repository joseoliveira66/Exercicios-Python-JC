# Estrutura de repetição while - Repetição com teste lógico

'''for c in range(1, 10):
    print(c)
print('FIM')'''

'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')'''

'''n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} pares e {} impares '.format(par, impar))



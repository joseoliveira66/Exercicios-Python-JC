#  Laços de repitição

'''for c in range(0, 6):
    print('OI')
print('FIM')'''

'''for c in range(1, 7):
    print(c)
print('FIM')'''


'''for c in range(6, 0, -1):
    print(c)
print('FIM')'''

'''for c in range(0, 12, 2):
    print(c)
print('FIM')'''

'''n = int(input('Digite um número: '))
for c in range(0, n+1, 2):
    print(c)
print('FIM')'''

'''i = int(input('Digite i inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
if p == 0:
    print('Zero não é válido. Digite um número maior que zero para "p"')
else:
    for c in range(i, f+1, p):
        print(c)
    print('FIM')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n
print('A soma dos números é {} '.format(s))

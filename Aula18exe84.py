# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves

dado = []
princ = []
mai = men = 0

while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))
    if len(princ) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        elif dado[1] < men:
            men = dado[1]
    princ.append(dado[:])
    dado.clear()

    parar = input('Quer continuar [S/N]: ').lower().upper()
    if parar == 'N':
        break
print('-=' * 40)
print(f'A quantidade de pessoas cadastradas foram {len(princ)}')
print(f'O maior peso foi de {mai} Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men} Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()

# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior_18 = 0
total_homens = 0
mulheres_menos_20 = 0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in ('M', 'F'):
        sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()[0]

    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = ' '
    while continuar not in ('S', 'N'):
        continuar = str(input('Deseja continuar, (S/N)? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Existem {maior_18} maiores de 18 anos. ')
print(f'Existem {total_homens} homens cadastrados. ')
print(f'Existem {mulheres_menos_20} mulheres menores de 20 anos. ')


# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0

'''while True:
    n = int(input('Digite um número. Se quiser parar digite 999: '))
    if n == 999:
        break
    cont += 1
    soma += n
print('Você digitou {} números e a soma entre eles é {} '.format(cont, soma))'''

num = 0
num = int(input('Digite um número. Se quiser parar, digite 999: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número. Se quiser parar, digite 999: '))
print('Você digitou {} números e a soma entre eles é {} '.format(cont, soma))

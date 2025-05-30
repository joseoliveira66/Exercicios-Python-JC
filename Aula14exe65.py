#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi
#  o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

qtde = soma = media = maior = menor = 0

resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtde += 1
    if qtde == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar digitando? [S/N]? ')).upper().strip()
media = soma / qtde
print('Você digitou {} números e a media entre eles é {} '.format(qtde, media))
print('O menor número digitado foi {} e o maior foi {} '.format(menor, maior))

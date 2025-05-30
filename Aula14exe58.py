# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
# até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time

numero = random.randint(0, 10)
palpites = 0
acertou = False

print('O computador pensou num número de 0 a 10 ')
print('Tente adinvinhar o número pensado pelo computador até acertar ')

while not acertou:
    numero_usuario = int(input('Digite seu palpite: '))
    palpites += 1
    print('Processando, aguarde! ')
    time.sleep(1)

    if numero_usuario == numero:
        acertou = True
        print('Parabéns!! Você acertou o número {} com {} palpites. '.format(numero, palpites))
    else:
        if numero_usuario < numero:
            print('Digite um numero maior: ')
        else:
            print('Digite um número menor: ')


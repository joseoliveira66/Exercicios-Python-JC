# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
numero = random.randint(0, 5)
numero_usuario = int(input('Tente adivinhar um numero de 0 a 5: '))
print('Processando, aguarde!!')
time.sleep(2)
if numero_usuario == numero:
    print('Você ganhou, Parabéns!! ')
else:
    print('Você perdeu, tente novamente. O número correto é {}'.format(numero))
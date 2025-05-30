# Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções de jogada são:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

print('-=' * 15)
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('O computador jogou {} '.format(itens[computador]))
print('O Jogador jogou {} '.format(itens[jogador]))
print('-=' * 15)

if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')
elif computador == 1: # Computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE!!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')
elif computador == 2: # Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')

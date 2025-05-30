# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.

import random

vitoria = 0
while True:
   jogador = int(input('Digite um número: '))
   computador = random.randint(0, 11)
   total = jogador + computador
   tipo = ' '
   while tipo not in 'PI':
       tipo = str(input('Par ou impar [P/I]? ')).strip().upper()
   print(f'Vocé jogou {jogador} e computador jogou {computador} e o total foi {total} ')
   print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
   if tipo == 'P':
       if total % 2 == 0:
           print('Você venceu!! ')
           vitoria += 1
       else:
           print('Você perdeu!! ')
           break
   elif tipo == 'I':
       if total % 2 == 1:
           print('Você venceu!! ')
           vitoria += 1
       else:
            print('Você perdeu!! ')
            break
   print('Vamos jogar novamente? ')
print(f'GAME OVER!! Você obteve {vitoria} vitórias')


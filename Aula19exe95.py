# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Digite o nome do jogador: '))
tot = int(input(f'Digite quantas partidas o jogador {jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'Digite o numero de gols na partida {c + 1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f' O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')
for i, v in enumerate(jogador['gols']):
    print(f'   ===> Na partida {i + 1} fez {v} glos.')
print(f'Foi um total de {jogador["total"]} gols. ')


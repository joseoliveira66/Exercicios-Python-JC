# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times = ('Cruzeiro', 'Botafogo', 'Flamengo', 'Atletico', 'Corinthias', 'Vasco', 'São Paulo', 'Chapecoense',
         'Goias', 'Brasiliense', 'Ceara', 'Curitiba', 'Grêmio', 'Internacional', 'Fluminense', 'Palmeiras',
         'Bahia', 'Colorado', 'Parana', 'Ituense')
print(f'Lista de times do Brasileirão: {times}')
print(f'Os cinco primeiros colocados são: {times[0:5]}')
#print(f'Os quatro últimos colocados são: {times[16:20]}')
print(f'Os quatro últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição. ')
'''for cont in range(0, len(times)):
    if times[cont] == 'Chapecoense':
        print(f'A Chapecoense está na {cont + 1}ª posição.')'''

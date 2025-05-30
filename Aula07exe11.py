# Calcular a area de uma parede e a qtde de tinta para pintar
alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
rend = float(input('Digite o rendimento da tinta: '))
tinta = area / rend
print('Uma parede com {:.2f} de altura e {:.2f} de largura, tem uma área total de {:.2f}. Com um rendimento de 1 litro para {} m² de parede, você precisará de {:.2f} litros de tinta.'.format(alt, larg, area, rend, tinta))

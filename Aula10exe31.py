# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
# de até 200Km e R$0,45 parta viagens mais longas.

km_viagem  = float(input('Quantos Km de distância você vai percorrer? '))
km1 = km_viagem * 0.50
km2 = km_viagem * 0.45
if km_viagem <= 200.00:
    print('Para uma viagem de {:.2f} Km você pagará R$ {:.2f}'.format(km_viagem, km1))
else:
    print('Para uma viagem de {:.2f} Km você pagará o valor de R$ {:.2f}'.format(km_viagem, km2))

# Simplificado
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
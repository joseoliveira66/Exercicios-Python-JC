# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final,
# mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

total_gasto = 0
prod_acima_1000 = 0
prod_mais_barato = ' '
preço_mais_barato = None

while True:
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preço = float(input('Digite o valor do produto em R$: '))

    total_gasto += preço

    if preço > 1000:
        prod_acima_1000 =+ 1
    if preço_mais_barato is None or preço < preço_mais_barato:
        preço_mais_barato = preço
        prod_mais_barato = nome
    '''continuar = str(input('Deseja continuar a venda [S/N]: ')).strip().upper()
    if continuar != 'S':
        break'''
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja contunuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na comra foi de R$ {total_gasto:.2f}. ')
print(f'{prod_acima_1000} custam acima de R$ 1.000. ')
print(f'O produto mais barato foi o {prod_mais_barato}. ')

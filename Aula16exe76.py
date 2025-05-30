# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular.

produto_preco = (('Arroz', 8.98),
                 ('Feijao', 6.78),
                 ('Macarrão', 5.32),
                 ('Manteiga', 5.84),
                 ('Óleo', 4.78),
                 ('Farinha', 3.56)
                 )
print('LISTAGEM DE PREÇOS')
print("-" * 32)
for produto, preco in produto_preco:
    print(f'{produto:.<20} R$ {preco:>7.2f}')
print("-" * 32)

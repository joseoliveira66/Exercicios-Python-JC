# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto, – à vista no cartão: 5% de desconto, - em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS OLIVEIRA '))

preço = float(input('Digite o valor do produto. R$ '))

print('''Formas de pagamento:
      [1] A vista dinheiro/cheque.
      [2] A vista no cartão.
      [3] 2 X no cartão.
      [4] 3 X ou mais no cartão.''')

pagamento = int(input('Escolha a forma de pagamento: '))

if pagamento == 1:
    print('O valor a pagar a vista em dinheiro/cheque é de R$ {:.2f}'.format(preço - (preço * 10/100)))
elif pagamento == 2:
    print('O valor a pagar à vista no cartão é de R$ {:.2f}'.format(preço - (preço * 5/100)))
elif pagamento == 3:
    parcela = preço / 2
    print('O valor a pagar em até 2X no cartão é de R$ {:.2f} em duas parcelas de R$ {:.2f}'.format(preço, parcela))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    vr_parc = (preço + (preço * 20/100)) / parcelas
    print('O valor a pagar em 3X ou mais no cartão será de R$ {:.2f} em {} parcelas de {:.2f} R$'.format(preço + (preço * 20/100), parcelas, vr_parc))
else:
    print('Código de pagamento inválido! Tente novamente! ')
    
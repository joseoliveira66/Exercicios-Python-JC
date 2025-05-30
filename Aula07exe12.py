prod = float(input('Digite o valor do produto R$ '))
desc = float(input('Digite o % de desconto: '))
vdesc = prod * desc
vprod = prod - vdesc
print('Valor original do produto R$ {:.2f}, percentual de desconto % {:.2f}'.format(prod, desc))
print('O valor do desconto em R$ {:.2f} e o valor a pagar é de R$ {:.2f}'.format(vdesc, vprod))

# Coversão de real para dólar
real = float(input('Quantos reais você tem? R$ '))
vdolar = 3.27
dolar = real * vdolar
print('Seus R$ {:.2f}, convertidos em dolar na cotação de US$ {:.2f} serão US$ {:.2f} dólares'.format(real, vdolar, dolar))

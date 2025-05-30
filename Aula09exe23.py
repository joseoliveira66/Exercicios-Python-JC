# leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

#numero = str(input('Digite um número de 0 a 9999: '))

#if numero.isdigit() and 0 <= int(numero) <= 9999:
    #numero_formatado = numero.zfill(4)

    #print('Análise do número: {}'.format(numero))
    #print('Unidade: {}'.format(numero_formatado[3]))
    #print('dezena: {}'.format(numero_formatado[2]))
    #print('Centena: {}'.format(numero_formatado[1]))
    #print('Milhar: {}'.format(numero_formatado[0]))

#else:
    #print('Por favor digite um número válido entre 0 e 9999: ')

num = int(input('Digite um número entre 0 e 99999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
ml = num // 10000 % 10
print('Análise do número: {}'.format(num))
print('Unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('Milhao: {}'.format(ml))

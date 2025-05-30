# Trabalhando com cores

#print('\033[7;30;44mOlá mundo!\033[m')

'''a = 3
b = 5
print('Os números são \033[32m{}\033[m e \033[31m{}\033[m '.format(a, b))'''

nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

#print('Prazer em te conhecer {}{}{}!! '.format(cores['pretoebranco'], nome, cores['limpa']))

print('Prazer em te conhecer {}{}{}!! '.format('\033[0;7;35m', nome, '\033[m'))

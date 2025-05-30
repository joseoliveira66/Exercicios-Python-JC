# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação
# novamente até ter um valor correto

'''sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo M/F: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite um sexo válido')
print('O sexo digitado foi {} '.format(sexo))'''

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados incorretos. Digite novamente seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(sexo))

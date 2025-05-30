# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome completo: ')).strip()
#if "SILVA" in nome:
    #print("O nome contém 'SILVA' ")
#else:
    #print("O nome não contém 'SILVA' ")

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

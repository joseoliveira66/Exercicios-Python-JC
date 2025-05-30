# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

#print('''Escolha uma das bases para conversão:
#[1] Binária
#[2] Octal
#[3] Hexadecimal''')


numero = int(input('Digite um número inteiro: '))

print('Escolha uma opção para conversão do número: ')
print('[1] para convertar para base binária')
print('[2] para converter em base Octal')
print('[3] para converter para base hexadecimal')
bin = bin(numero)[2:]
octal = oct(numero)[2:]
hexa = hex(numero)[2:]

opcao = int(input('Para qual base você quer converter o número digitado? '))
if opcao == 1:
    print('O numero {} convertido para a base binária é {}'.format(numero, bin))
elif opcao == 2:
    print('O número {} convertido para a base Octal é {}'.format(numero, octal))
elif opcao == 3:
    print('O número {} convertido para a base hexadecimal é {}'.format(numero, hexa))
else:
    print('Digite uma opção válida')

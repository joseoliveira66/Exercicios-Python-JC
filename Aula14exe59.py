# Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números
# [ 5 ] sair do programa

import time

while True:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    while True:
        print('\nEscolha uma opção: ')
        print('[ 1 ] - Somar os valores: ')
        print('[ 2 ] - Multiplicar os valores: ')
        print('[ 3 ] - Maior valor: ')
        print('[ 4 ] - Digite novos números: ')
        print('[ 5 ] - Sair do programa: ')
        opcao = int(input('Digite sua opção: '))
        time.sleep(1)
        if opcao == 1:
            resultado = n1 + n2
            print('A soma de {} e {} é igual a {} '.format(n1, n2, resultado))
        elif opcao == 2:
            resultado = n1 * n2
            print('A multiplicação de {} por {} é igual a {} '.format(n1, n2, resultado))
        elif opcao == 3:
            resultado = max(n1, n2)
            print('O maior número entre {} e {} é {} '.format(n1, n2, resultado))
        elif opcao == 4:
            break
        elif opcao == 5:
            print('Saindo do sistema!! ')
            time.sleep(1)
            exit()
        else:
            print('Opação inválida. Tente novamente: ')


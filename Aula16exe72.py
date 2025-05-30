# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        num_dig = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num_dig <= 20:
            break
        print('Tente novamente. ', end="")

    print(f'Voce digitou o número {numero[num_dig]}')

    continuar = str(input('Deseja continuar? [S/N]. ')).strip().upper()
    if continuar != 'S':
        break


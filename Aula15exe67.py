# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será
# interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Digite um numero para o calculo da tabuada: '))
    if numero < 0:
        break
    print(f'A tabuada do número {numero} é: ')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero}  X  {i} =   {resultado}')
    continuar = str(input('Deseja digitar outro numero? [S/N] ')).strip().upper()
    if continuar != 'S':
        break
print('Fim do cálculo! ')

# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número de 1 a 10 para o calculo da tabuada: '))

print('A tabuada do número {} é: '.format(numero))
for i in range(1, 11):
    resultado = numero * i
    print('{:2} X {:2} = {:2} '.format(numero, i, resultado)) # posso fazer a formula do resultado dentro do print


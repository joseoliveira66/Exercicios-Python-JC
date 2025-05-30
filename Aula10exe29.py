# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade aferida: '))
vr_multa = 7.00
excesso = velocidade - 80
if velocidade <= 80.00:
    print('Sua velocidade foi de {:.2f} Km/h e você está dentro do limite permitido '.format(velocidade))
else:
    multa = (velocidade - 80.00) * 7.00
    print('Sua velocidade aferida foi de {:.2f} Km/h. Você passou {:.2f} Km/h acima do permitido que é 80Km/h e o valor da sua multa é de R$ {:.2f}'.format(velocidade, excesso, multa))
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:  – IMC abaixo de 18,5: Abaixo do Peso, – Entre 18,5 e 25: Peso Ideal, – 25 até 30: Sobrepeso
# 30 até 40: Obesidade, – Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('Seu peso é {:.2f}, sua altura é {:.2f}, seu IMC é {:.2f}. VOCÊ ESTÁ ABAIXO DO PESO!! '.format(peso, altura, IMC))
elif IMC >= 18.5 and IMC < 25:
    print('Seu peso é {:.2f}, sua altura é {:.2f}, seu IMC é {:.2f}. VOCÊ ESTÁ NO PESO IDEAL!! '.format(peso, altura, IMC))
elif IMC >= 25 and IMC < 30:
    print('Seu peso é {:.2f}, sua altura é {:.2f}, seu IMC é {:.2f}. VOCÊ ESTÁ COM SOBREPESO. CUIDE-SE!! '.format(peso, altura, IMC))
elif IMC >=30 and IMC < 40:
    print('Seu peso é {:.2f}, sua altura é {:.2f}, seu IMC é {:.2f}. VOCÊ ESTÁ OBESO. CUIDE-SE!!!! '.format(peso, altura, IMC))
else:
    print('''
    Seu peso é {:.2f},
    sua altura é {:.2f},
    seu IMC é {:.2f}.
    VOCÊ ESTÁ COM OBESIDADE MÓRBIDA. PROCURE UM MÉDICO!! '''.format(peso, altura, IMC))

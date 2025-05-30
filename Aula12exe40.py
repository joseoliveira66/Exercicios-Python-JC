# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#  – Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO, Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print("Sua primeira nota foi {:.2f}, sua segunda nota foi {:.2f}. Sua média foi {:.2f}. Com essa média, você foi REPROVADO!".format(nota1, nota2, media))
elif media >= 5 and media < 7:
    print("Sua primeira nota foi {:.2f}, sua segunda nota foi {:.2f}. Sua média foi {:.2f}. Com essa média, você está de recuperação, ESTUDE!!!".format(nota1, nota2, media))
else:
    print("Sua primeira nota foi {:.2f}, sua segunda nota foi {:.2f}. Sua média foi {:.2f}. Com essa média, você FOI APROVADO!!".format(nota1, nota2, media))

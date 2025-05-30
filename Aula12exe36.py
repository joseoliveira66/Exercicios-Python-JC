# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vr_casa = float(input('Qual o valor do imóvel R$ '))
salario = float(input('Qual o valor do seu salario R$ '))
prazo = int(input('Em quantos anos pretende pagar o empréstimo: '))

prestacao = vr_casa / (prazo * 12)
minimo = salario * 30/100
if prestacao <= minimo:
    print('Para um imóvel de R$ {:.2f} a prestação será de R$ {:.2f}. Seu emprestimo foi \033[4;34m autorizado \033[m'.format(vr_casa, prestacao))
else:
    print('Para um imóvel de R$ {:.2f} a prestação será de R$ {:.2f}. Seu emprestimo foi \033[4;31m Negado \033[m'.format(vr_casa, prestacao))

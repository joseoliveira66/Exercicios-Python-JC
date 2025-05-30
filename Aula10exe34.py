# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário atual. R$ '))
s1 = salario + (salario * 10/100)
s2 = salario + (salario * 15/100)
if salario <= 1250.00:
    print('Seu salário atual é R$ {:.2f}. O % do seu aumento foi de 15% gerando um valor de R$ {:.2f} e totalizando R$ {:.2f} '.format(salario, (s2 - salario), s2))
else:
    print('Seu salário atual é R$ {:.2f}. O % do seu aumento foi de 10% gerando um valor de R$ {:.2f} e totalizando R$ {:.2f} '.format(salario, (s1 - salario), s1))

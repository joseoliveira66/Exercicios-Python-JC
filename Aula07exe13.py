salario = float(input('Digite seu salario R$ '))
aumento = float(input('Digite o percentual de aumento % '))
novo_sal = salario + (salario * aumento)
print('Seu novo salario e R$ {:.2f}'.format(novo_sal))
